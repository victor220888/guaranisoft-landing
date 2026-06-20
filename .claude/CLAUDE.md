# CLAUDE.md — Landing GuaraníSoft

## Context
This is the landing page for Ñande ERP, a Paraguayan ERP system built by GuaraníSoft.
The landing is a separate project from the ERP itself — different repo, different deploy.

## Quick start
```bash
cd /home/victor/landing-guaranisoft
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
cp .env.example .env  # edit with real credentials
.venv/bin/uvicorn main:app --reload
```

## Architecture
- **FastAPI** app with 4 routes: `/`, `/contacto`, `/health`, `/admin/leads`
- **Jinja2** single-page template (`templates/index.html`)
- **Bootstrap 5** via CDN + custom CSS (`static/css/landing.css`)
- **Google Sheets** (primary persistence via gspread)
- **SQLite** (fallback, local only — not persistent on Render Free)
- **SMTP** (Gmail, background task with 10s timeout)

## Key files
- `main.py` — FastAPI app, routes, email logic
- `sheets.py` — Google Sheets integration (gspread)
- `db.py` — SQLite fallback
- `templates/index.html` — Full landing page (7 sections, AJAX form)
- `static/css/landing.css` — Custom styles
- `static/img/` — Logo SVGs (from ERP branding v2.0)

## Form flow
1. User fills form → `fetch('/contacto', {POST})`
2. `sheets.append_to_sheet()` → Google Sheet "Leads GuaraníSoft" / "Ñande ERP" tab
3. `db.save_lead()` → SQLite (local fallback)
4. `asyncio.create_task(_send_email_async())` → background SMTP with 10s timeout
5. Returns `{"status": "ok"}` JSON
6. JS shows success message, resets form
7. Rate limit: 60s per IP (returns 429, JS shows yellow warning)

## Environment variables
```
SMTP_USER=your@gmail.com
SMTP_PASSWORD=your_app_password
CONTACT_EMAIL=contacto@guaranisof.com
ADMIN_USER=admin
ADMIN_PASSWORD=change_this
```

## Secret Files
- `service_account.json` — Google Cloud service account key
- On Render: uploaded as Secret File → lives in `/etc/secrets/`
- On local: placed in project root
- **NEVER commit this file** (it's in .gitignore)
- `sheets.py` searches both locations automatically

## Deploy (Render)
- **Build:** `pip install -r requirements.txt`
- **Start:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
- **Plan:** Free (512MB RAM, spins down after 15min idle)
- **Auto-deploy:** on push to `main` branch
- **Custom domain:** guaranisof.com (via Cloudflare DNS)

## Known issues
- **Render blocks SMTP port 587** — emails don't send in production. Leads still save to Google Sheets. Need alternative: SendGrid free, Mailgun, or similar.
- **Render Free cold start** — first request after idle takes 30-50s. Not fixable on free tier.
- **SQLite not persistent** — Render Free disk is ephemeral. Google Sheets is the primary store.
- **Rate limit is in-memory** — resets on app restart. Not a problem for low traffic.

## Branding
- **Logo:** Ñ pixelada (morado #5B2A86) + "ande ERP" text + mburucuyá watermark
- **Colors:** morado #5B2A86, verde #4A7C59, gris #F5F7FA
- **Slogan:** "ERP paraguayo. Cumplimiento real. Soporte local."
- **Do not change colors or logo without owner authorization**

## Owner
Victor Roman — victor.roman.czu@gmail.com — +595 992 504 620

## Related repos
- **ERP:** `/home/victor/erp-system/` (private, local only)
- **Landing:** this repo — https://github.com/victor220888/guaranisoft-landing

## Documentation
- `docs/GUIA_DEPLOY_RENDER.md` — Step-by-step Render deploy guide
- `docs/GUIA_DNS_CLOUDFLARE_RENDER.md` — DNS configuration guide
- `docs/ARQUITECTURA.md` — Full architecture documentation
- `docs/landing_content.md` — Content source of truth (features, sections)

## Git conventions
- Branch: `main`
- Commits in Spanish, conventional commits format
- Never commit: `.env`, `service_account.json`, `leads.db`, `.venv/`
