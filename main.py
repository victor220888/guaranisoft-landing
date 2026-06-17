"""
Landing Page — Ñande ERP / GuaraníSoft
Deploy: Railway o Render
Run: uvicorn main:app --host 0.0.0.0 --port 8000
"""

import os
import time
from collections import defaultdict
from pathlib import Path

import db          # SQLite (fallback local)
import sheets      # Google Sheets (primario, persistente)
import secrets

from fastapi import FastAPI, Form, Request, Depends, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
app = FastAPI(title="Ñande ERP — GuaraníSoft", docs_url=None, redoc_url=None)

db.init_db()

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

# ── Rate limiting simple ────────────────────────────────────────────────────
_last_sent: dict[str, float] = defaultdict(float)
RATE_LIMIT_SECONDS = 60

security = HTTPBasic()


def verify_admin(credentials: HTTPBasicCredentials = Depends(security)):
    correct_user = secrets.compare_digest(credentials.username, os.getenv("ADMIN_USER", "admin"))
    correct_pass = secrets.compare_digest(credentials.password, os.getenv("ADMIN_PASSWORD", "secret"))
    if not (correct_user and correct_pass):
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    return True


@app.get("/admin/leads")
async def ver_leads(admin: bool = Depends(verify_admin)):
    leads = db.get_all_leads()
    return {"leads": leads}


# ── Página principal ────────────────────────────────────────────────────────
@app.get("/", response_class=HTMLResponse)
async def index(request: Request, sent: str | None = None):
    return templates.TemplateResponse(request, "index.html", {"sent": sent == "1"})


# ── Formulario de contacto ─────────────────────────────────────────────────
@app.post("/contacto")
async def contacto(
    request: Request,
    nombre: str = Form(...),
    empresa: str = Form(""),
    telefono: str = Form(""),
    email: str = Form(...),
    mensaje: str = Form(...),
):
    client_ip = request.client.host if request.client else "unknown"

    # Rate limit
    now = time.time()
    if now - _last_sent[client_ip] < RATE_LIMIT_SECONDS:
        return RedirectResponse(url="/#contacto?sent=rate", status_code=303)
    _last_sent[client_ip] = now

    # 1. Guardar en Google Sheets (primario, persistente)
    sheets.append_to_sheet(nombre, empresa, telefono, email, mensaje)

    # 2. Guardar en SQLite (fallback local)
    db.save_lead(nombre, empresa, telefono, email, mensaje)

    # 3. Enviar email
    smtp_user = os.getenv("SMTP_USER", "")
    smtp_pass = os.getenv("SMTP_PASSWORD", "")
    contact_email = os.getenv("CONTACT_EMAIL", "contacto@guaranisof.com")

    body = f"""\
Nuevo contacto desde la landing page de Ñande ERP

Nombre:    {nombre}
Empresa:   {empresa or '—'}
Teléfono:  {telefono or '—'}
Email:     {email}

Mensaje:
{mensaje}
"""

    if smtp_user and smtp_pass:
        try:
            import aiosmtplib
            from email.mime.text import MIMEText
            from email.mime.multipart import MIMEMultipart

            msg = MIMEMultipart()
            msg["From"] = smtp_user
            msg["To"] = contact_email
            msg["Reply-To"] = email
            msg["Subject"] = f"Contacto landing — {nombre}"
            msg.attach(MIMEText(body, "plain", "utf-8"))

            await aiosmtplib.send(
                msg,
                hostname="smtp.gmail.com",
                port=587,
                start_tls=True,
                username=smtp_user,
                password=smtp_pass,
            )
        except Exception as e:
            print(f"[SMTP ERROR] {e}")

    return RedirectResponse(url="/?sent=1#contacto", status_code=303)


# ── Health check (para Railway/Render) ──────────────────────────────────────
@app.get("/health")
async def health():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
