# AGENTS.md — Landing GuaraníSoft

## Proyecto
Landing page pública para Ñande ERP / GuaraníSoft. Repo separado del ERP.
No comparte código ni base de datos con el ERP.

## Info esencial
- **Repo:** https://github.com/victor220888/guaranisoft-landing
- **Local:** `/home/victor/landing-guaranisoft/`
- **URL producción:** https://guaranisof.com
- **URL Render:** https://guaranisoft-landing.onrender.com
- **Stack:** Python 3.12, FastAPI, Jinja2, Bootstrap 5, SQLite, Google Sheets

## Reglas
- `service_account.json` NUNCA se sube a git (está en .gitignore)
- `leads.db` NUNCA se sube a git
- `.env` NUNCA se sube a git
- No cambiar la paleta de marca sin autorización (morado #5B2A86, verde #4A7C59)
- No inventar features del ERP — el contenido está en `docs/landing_content.md`
- El Owner es Victor Roman. Solo él autoriza cambios

## Owner
- **Victor Roman** — Arquitecto y Analista/Desarrollador
- WhatsApp: +595 992 504 620
- Email: victor.roman.czu@gmail.com
- LinkedIn: https://www.linkedin.com/in/victor-roman-226bb155/

## Empresa
- **GuaraníSoft** — Software para empresas paraguayas
- **Producto:** Ñande ERP
- **Dominio:** guaranisof.com (sin "t" — el .com con "t" estaba tomado)
- Pendiente: comprar guaranisoft.com en mayo 2027, no renovar guaranisof.com

## Emails (Cloudflare Email Routing)
- ventas@guaranisof.com → Victor
- soporte@guaranisof.com → Victor
- contacto@guaranisof.com → Victor

## Infraestructura
- **Hosting:** Render Free Tier (se duerme tras 15 min sin tráfico)
- **DNS:** Cloudflare (A record → 216.24.57.1, CNAME www → onrender.com)
- **Email SMTP:** Render bloquea puerto 587 — el email funciona en local pero no en producción. Pendiente alternativa (SendGrid free, etc.)

## Estructura de archivos
```
landing-guaranisoft/
├── main.py              # FastAPI — rutas + lógica
├── db.py                # SQLite (fallback local)
├── sheets.py            # Google Sheets (primario, persistente)
├── requirements.txt
├── .env.example
├── .gitignore
├── templates/
│   └── index.html       # Landing completa (7 secciones)
├── static/
│   ├── css/landing.css
│   └── img/             # logo-eslogan, logo-compacto, favicon (SVG)
└── docs/
    ├── GUIA_DEPLOY_RENDER.md
    ├── GUIA_DNS_CLOUDFLARE_RENDER.md
    ├── ARQUITECTURA.md
    └── landing_content.md
```

## Rutas de la app
| Método | Path | Descripción |
|--------|------|-------------|
| GET | `/` | Landing page |
| POST | `/contacto` | Formulario → JSON {status: ok} |
| GET | `/health` | Health check |
| GET | `/admin/leads` | Ver leads (HTTP Basic Auth) |

## Variables de entorno
| Variable | Descripción |
|----------|-------------|
| `SMTP_USER` | Gmail para enviar emails |
| `SMTP_PASSWORD` | App Password de Gmail |
| `CONTACT_EMAIL` | Email destino (contacto@guaranisof.com) |
| `ADMIN_USER` | Usuario para /admin/leads |
| `ADMIN_PASSWORD` | Password para /admin/leads |

## Secret Files (Render)
- `service_account.json` — credenciales Google Cloud (en /etc/secrets/)

## Flujo del formulario
1. Usuario llena formulario → fetch POST /contacto
2. Google Sheets: guarda en pestaña "Ñande ERP" (primario)
3. SQLite: guarda local (fallback)
4. SMTP: intenta en background con timeout 10s (probablemente falla en Render)
5. Responde JSON {status: ok}
6. JS muestra mensaje de éxito
7. Rate limit: 1 envío por IP cada 60s (muestra alert amarillo si se bloquea)

## Logos
Los 3 SVG vienen del ERP (branding v2.0):
- `logo-eslogan.svg` (P3) — Hero
- `logo-compacto.svg` (P1) — Navbar
- `favicon.svg` (P4) — Favicon

Paleta: morado #5B2A86 + verde #4A7C59 + gris #F5F7FA

## Deploy
Ver `docs/GUIA_DEPLOY_RENDER.md` para paso a paso.
- Build: `pip install -r requirements.txt`
- Start: `uvicorn main:app --host 0.0.0.0 --port $PORT`
- Auto-deploy on commit (main branch)

## Pendientes
- SMTP en Render: investigar alternativa (SendGrid, Mailgun, etc.)
- Verificar cold start de Render Free (puede tardar 30-50s)
- Deploy del ERP en la nube con Docker (proyecto separado)
- Merge de ramas del ERP (feat/branding-nande-erp, feat/ayuda-categorias)
- Actualizar referencias guaranisoft.com → guaranisof.com en el ERP
