# Guía de Configuración DNS — Cloudflare + Render

> Cómo apuntar tu dominio de Cloudflare a una app en Render
> Basado en la configuración real de `guaranisof.com` → Render

---

## ¿Qué es DNS?

DNS es como la guía telefónica de internet. Cuando alguien escribe `guaranisof.com` en el navegador, DNS le dice a qué servidor ir. Nosotros tenemos que decirle: "guaranisof.com apunta a Render".

## Conceptos

| Término | Qué es | Ejemplo |
|---------|--------|---------|
| **Dominio** | La dirección que comprás | `guaranisof.com` |
| **Registrar** | Donde lo compraste | Cloudflare |
| **Hosting** | Donde corre tu app | Render |
| **DNS Record** | Una instrucción que dice dónde ir | A, CNAME, MX, TXT |
| **Root domain** | El dominio sin www | `guaranisof.com` |
| **Subdomain** | Con prefijo | `www.guaranisof.com` |

---

## Los DNS Records que necesitas

Para que `guaranisof.com` y `www.guaranisof.com` apunten a Render necesitás 2 registros:

### Registro A (dominio principal)
Apunta `guaranisof.com` (sin www) a la IP de Render.

| Campo | Valor |
|-------|-------|
| Type | **A** |
| Name | `@` |
| IPv4 address | `216.24.57.1` (IP que da Render) |
| Proxy status | **DNS only** (gris) ← ver nota abajo |
| TTL | Auto |

### Registro CNAME (www)
Apunta `www.guaranisof.com` al dominio de Render.

| Campo | Valor |
|-------|-------|
| Type | **CNAME** |
| Name | `www` |
| Target | `guaranisoft-landing.onrender.com` |
| Proxy status | **DNS only** (gris) |
| TTL | Auto |

---

## Paso a paso en Cloudflare

### 1. Entrar al panel de DNS

1. Entrá a https://dash.cloudflare.com
2. Seleccioná tu dominio (`guaranisof.com`)
3. Menú izquierda → **DNS** → **Records**

### 2. Agregar registro A

1. Click **"Add record"**
2. **Type:** `A`
3. **Name:** `@` (significa el dominio raíz, `guaranisof.com`)
4. **IPv4 address:** `216.24.57.1` (la IP que te da Render)
5. **Proxy status:** Click la nube naranja hasta que quede **gris** ("DNS only")
6. **TTL:** Auto
7. **Save**

### 3. Agregar registro CNAME

1. Click **"Add record"**
2. **Type:** `CNAME`
3. **Name:** `www`
4. **Target:** `guaranisoft-landing.onrender.com`
5. **Proxy status:** Click la nube hasta que quede **gris** ("DNS only")
6. **TTL:** Auto
7. **Save**

### 4. Verificar en Render

1. Volvé a Render → tu servicio → **Settings** → **Custom Domains**
2. Click **"Verify"**
3. Si dice verificado ✅, listo
4. Si falla, esperá 5-10 minutos y probá de nuevo (DNS tarda en propagagar)

---

## ⚠️ Proxy status: DNS only (gris) vs Proxied (naranja)

### Durante la verificación: DNS only (gris)
Render necesita verificar que sos el dueño del dominio. Si Cloudflare está en modo "Proxied" (naranja), oculta la IP real y Render no puede verificar. Por eso **tenés que ponerlo en gris** al principio.

### Después de verificado: podés activar Proxied (naranja)
Una vez que Render verificó el dominio, podés cambiar a "Proxied" (naranja) para obtener:
- **SSL automático** (HTTPS sin configurar certificados)
- **CDN** (tu página carga más rápido en otros países)
- **Protección DDoS** (Cloudflare bloquea ataques)
- **Esconder la IP** de tu servidor

Para activarlo:
1. Cloudflare → DNS → Records
2. Editá el registro A → Proxy status → **Proxied** (naranja)
3. Editá el registro CNAME → Proxy status → **Proxied** (naranja)
4. **Save**

La app sigue funcionando igual, pero con los beneficios extra.

---

## Registros de Email (Cloudflare Email Routing)

Si configuraste Email Routing en Cloudflare (como hicimos con `ventas@`, `soporte@`, `contacto@guaranisof.com`), vas a ver estos registros adicionales que **NO hay que tocar**:

| Type | Name | Content | Para qué sirve |
|------|------|---------|----------------|
| MX | `@` | `route1.mx.cloudflare.net` | Recibe emails (prioridad 84) |
| MX | `@` | `route2.mx.cloudflare.net` | Recibe emails (prioridad 6) |
| MX | `@` | `route3.mx.cloudflare.net` | Recibe emails (prioridad 26) |
| TXT | `@` | `v=spf1 include:_spf.mx.cloudflare.net ~all` | SPF — evita que te marquen como spam |
| TXT | `cf2024-1._domainkey` | `v=DKIM1; ...` | DKIM — firma los emails |

Estos los agrega Cloudflare automáticamente cuando activás Email Routing. No los modifiques ni los borres.

---

## Cómo se ven todos los registros juntos

Después de configurar todo, tu DNS debería verse así (7 registros):

| Type | Name | Content | Proxy |
|------|------|---------|-------|
| A | `@` | `216.24.57.1` | DNS only o Proxied |
| CNAME | `www` | `guaranisoft-landing.onrender.com` | DNS only o Proxied |
| MX | `@` | `route1.mx.cloudflare.net` | DNS only |
| MX | `@` | `route2.mx.cloudflare.net` | DNS only |
| MX | `@` | `route3.mx.cloudflare.net` | DNS only |
| TXT | `@` | `v=spf1 include:_spf.mx.cloudflare.net ~all` | DNS only |
| TXT | `cf2024-1._domainkey` | `v=DKIM1; ...` | DNS only |

---

## Resumen visual

```
Usuario escribe guaranisof.com
        ↓
Cloudflare DNS busca el registro A
        ↓
Encuentra: @ → 216.24.57.1
        ↓
Va a Render (donde corre la app)
        ↓
Render sirve la landing page
        ↓
Usuario ve la página
```

Para emails:
```
Alguien escribe a contacto@guaranisof.com
        ↓
Cloudflare MX recibe el email
        ↓
Email Routing redirige a tu Gmail
        ↓
Te llega a tu bandeja de entrada
```

---

## Problemas comunes

### "We weren't able to verify guaranisof.com"
**Causa 1:** Los registros están en "Proxied" (naranja) en vez de "DNS only" (gris).
**Solución:** Cambiar a gris y volver a verificar.

**Causa 2:** Los registros no se agregaron correctamente.
**Solución:** Verificar que el registro A tenga la IP correcta (`216.24.57.1`) y el CNAME apunte a `guaranisoft-landing.onrender.com`.

**Causa 3:** DNS todavía no propagó.
**Solución:** Esperar 5-30 minutos. A veces tarda.

### La página no carga en guaranisof.com pero sí en onrender.com
**Causa:** El registro A o CNAME no está bien configurado.
**Solución:** Verificar los registros en Cloudflare. Probar con https://dnschecker.org para ver si el DNS ya propagó.

### El email no llega
**Causa:** Falta SPF o DKIM, o Email Routing no está activado.
**Solución:** En Cloudflare → Email → Email Routing → verificar que esté activado y las rutas configuradas.

### Hay un registro CAA que bloquea
**Causa:** Cloudflare a veces agrega registros CAA que restringen qué CA puede emitir certificados.
**Solución:** Borrar el registro CAA temporalmente, verificar en Render, y después volver a agregar si querés.

---

## Verificar que todo funciona

1. **Página web:** Abrí https://guaranisof.com → debería mostrar la landing
2. **www:** Abrí https://www.guaranisof.com → debería mostrar lo mismo
3. **Email:** Escribí a contacto@guaranisof.com → debería llegar a tu Gmail
4. **SSL:** La URL debe decir `https://` (candado verde). Si no, activá "Proxied" en Cloudflare para que dé SSL automático.

---

*Documentado el 2026-06-17 basado en la configuración real de guaranisof.com en Cloudflare + Render.*
