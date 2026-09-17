# BRANDING.md — GuaraníSoft / Ñande ERP

## Empresa

- **Producto:** Ñande ERP (sistema de gestión para empresas paraguayas)
- **Empresa:** GuaraníSoft
- **Dominio:** guaranisof.com
- **Stack:** Python 3.12, FastAPI, MySQL, Bootstrap 5

---

## Logo v2.0 — Especificaciones

### Concepto

- Ñ pixelada (letra característica del guaraní) como símbolo
- "ande ERP" como texto (ande = "nosotros" en guaraní)
- Flor de mburucuyá (passion flower) como marca de agua/acento
- Homenaje a Paraguay: la Ñ (idioma), el mburucuyá (flora nacional)

### Paleta de colores

| Color | Hex | Uso |
|-------|-----|-----|
| Morado | #5B2A86 | Primario — Ñ pixelada, botones, títulos |
| Verde | #4A7C59 | Secundario — "ERP" texto, checks, acentos |
| Gris claro | #F5F7FA | Fondos |
| Gris texto | #2D2D2D | Texto principal |
| Gris medio | #5A6470 | Eslogan |

### Modo oscuro

| Color | Hex |
|-------|-----|
| Morado claro | #9B6DC4 |
| Verde claro | #6FB07F |

### 5 archivos SVG finales

1. **P1_compacto_claro.svg** — Navbar fondo blanco (logo-compacto.svg)
2. **P2_compacto_oscuro.svg** — Navbar fondo oscuro (logo-compacto-dark.svg)
3. **P3_con_eslogan.svg** — Login/material comercial (logo-eslogan.svg)
4. **P4_icono.svg** — Favicon/app icon (favicon.svg)
5. **P5_avatar.svg** — Redes sociales (avatar.svg)

### Construcción de la Ñ pixelada

- Grid de píxeles cuadrados con border-radius suave (rx=1)
- Columnas: 3 verticales + diagonales conectando
- Tamaño píxel: 6x6 (navbar), 5x5 (icono)
- Los píxeles superiores (tilde de la Ñ) son verde #4A7C59
- El cuerpo de la Ñ es morado #5B2A86

### Texto

- "ande" en morado #5B2A86, font-weight 700
- "ERP" en verde #4A7C59, font-weight 700
- Font family: 'Segoe UI', sans-serif
- Eslogan: "ERP paraguayo. Cumplimiento real. Soporte local." en gris #5A6470, font-weight 400, font-size 12px

### Flor de mburucuyá (marca de agua)

- 6 pétalos grandes (morado) + 6 pétalos pequeños (verde, 70% opacidad)
- Círculo central verde
- Opacidad: 18% (modo claro), 22% (modo oscuro)
- Posición: centrada detrás del logo, no compite con la Ñ
- En P4/P5 (icono/avatar): desplazada a x=118 para no tapar la Ñ

### Ubicación de los archivos

- Workspace: docs/logo_conceptos/P1-P5
- ERP (WSL): /home/victor/erp-system/src/static/img/
- Landing: /home/victor/landing-guaranisoft/static/img/

## Tipografía

- **Titles/UI:** Plus Jakarta Sans (Google Fonts, gratis) — pesos 700/600/500
- **Body text:** Inter — pesos 400/300
- Pesos: 700 bold (títulos, logo), 600 semibold (botones, labels), 500 medium (nav), 400 regular (body), 300 light (hero)

## Arquitectura de marca

- **Marca comercial:** Ñande ERP (producto visible para clientes)
- **Empresa desarrolladora:** GuaraníSoft (razón social, contratos, docs técnicas)
- **Futura suite:** Ñande CRM, Ñande POS, Ñande Nómina, Ñande BI

## Dominios y presencia

- guaranisof.com — registrado (Cloudflare)
- nandeerp.com.py — verificar disponibilidad
- nandeerp.com — verificar disponibilidad
- Handles sugeridos: @nande.erp (IG/TikTok), /nandeerp (FB), /company/nande-erp (LinkedIn)

## Elementos a evitar

No usar: hojas, árboles, plantas, agricultura, iconografía ecológica, efectos metálicos, 3D, sombras excesivas, gráficos bursátiles genéricos.

## Guidelines de uso del logo

- Tamaño mínimo: 24px digital, 15mm impreso
- Padding mínimo: 1x altura del ícono
- Sobre fotos: usar versión avatar (P5) o fondo sólido
- No estirar, no distorsionar, no cambiar colores, no añadir efectos
- El logo es plano, siempre

## Emails

- ventas@guaranisof.com
- soporte@guaranisof.com
- contacto@guaranisof.com
- Todos redirigen a Gmail via Cloudflare Email Routing
