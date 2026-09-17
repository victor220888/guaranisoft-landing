# Propuesta de rediseño — guaranisof.com

**Fecha:** 2026-06-18
**Autor:** Tork
**Aprobado por:** Pendiente

---

## Resumen

La landing actual tiene buena estructura y copy, pero falla en ejecución visual: no muestra el producto, usa emojis como iconos, no tiene prueba social, y promete un módulo SIFEN que está en desarrollo. Esta propuesta corrige esos problemas y eleva la página al nivel de un producto profesional.

---

## 1. Ajustes de contenido

### 1.1 SIFEN — de "completo" a "a medida"

**Texto actual:**
> 7 tipos de DTE: factura, nota de crédito, nota de débito, autofactura, nota de remisión, retención, exportación. Firma digital, QR, lotes, eventos, consulta CDC. SIFEN v150.

**Texto propuesto:**
> Facturación electrónica SIFEN desarrollada a medida para tu empresa. Implementamos los tipos de DTE que necesitás, con firma digital, QR y gestión de lotes. Cumplimiento SIFEN v150.

**Justificación:** SIFEN está en fase inicial. Prometer 7 tipos de DTE completos es vender algo que no existe todavía. "A medida" es honesto y comercialmente fuerte — le dice al cliente que se adapta a sus necesidades.

### 1.2 Stats — de developer a usuario

**Stats actuales:**
- 96 tablas de datos
- 350+ endpoints
- 7 tipos de DTE SIFEN
- 100% cumplimiento Ley 6380

**Stats propuestas:**
- Instalación en menos de 48 horas
- Soporte directo por WhatsApp (no call center)
- 9 módulos integrados en un solo sistema
- Cumplimiento Ley 6380/2019, RG 49/14 y RESIMPLE

**Justificación:** "Tablas" y "endpoints" son métricas de desarrollador. El cliente no entiende ni le importan. Las nuevas métricas hablan de lo que el cliente quiere saber: ¿cuánto tarda?, ¿cómo me atendés?, ¿qué tengo?, ¿cumple?

### 1.3 Sección de precios — agregar referencia

**Actual:**
> "Cada empresa es diferente. Comprás lo que necesitás." → "Consultá por precio"

**Propuesto:**
> **Licencia única + mantenimiento mensual**
> 
> - Base: Ventas, compras, inventario, cajas, libro IVA, retenciones — **desde Gs. 4.500.000**
> - Módulos: SIFEN (a medida), Tributario, Contabilidad, Dashboard, Préstamos — se activan por empresa
> - Soporte: WhatsApp directo, no call center
> - Instalación: Local en Windows, sin dependencia de internet
> - Capacitación: Incluida en la instalación
> 
> *[Consultá por precio según tu combinación de módulos]*

**Justificación:** Un "desde" filtra curiosos y califica leads. No compromete la flexibilidad del modelo modular. Si el precio orientativo no es Gs. 4.500.000, ajustalo — pero tener un número ancla la conversación comercial.

### 1.4 Footer — agregar

**Actual:** No existe footer.

**Propuesto:**
```
GuaraníSoft · Desarrollo de software paraguayo
guaranisof.com · ventas@guaranisof.com · +595 992 504 620
[Logo compacto] · [Íconos de redes sociales] · © 2026
```

---

## 2. Ajustes visuales

### 2.1 Screenshots del producto

**Ubicación de las capturas ya tomadas:** `workspace/screenshots/screenshots/`

**Integración propuesta:**

| Sección | Captura | Uso |
|---------|---------|-----|
| Hero | dashboard.png | Mockup del dashboard con overlay del logo Ñ pixelada |
| "¿Por qué Ñande ERP?" | contabilidad.png | Plan de cuentas al lado del texto sobre cumplimiento |
| Sección módulos | Una captura por módulo (hover o click) | Reemplaza los emojis |
| "Cómo funciona" | Dashboard o ventas | Ilustra cada paso |
| Gallería/Carousel | dashboard + sifen + ventas + cajas | Slider con las 4 mejores |

**Tratamiento:**
- Recortar el navegador (ya hecho, capturas limpias)
- Difuminar datos sensibles si los hay
- Exportar a WebP para web (menor peso)
- Mobile: usar las capturas de 375px

### 2.2 Iconos SVG para los 9 módulos

**Reemplazar emojis por iconos SVG line-art con la paleta de marca.**

Diseño propuesto:
- Estilo: line-art, trazo 2px, sin relleno
- Color: morado #5B2A86 para el trazo, verde #4A7C59 para acentos
- Tamaño: 48x48px en desktop, 32x32px en mobile
- Border-radius suave en el contenedor (8px)

Módulos y conceptos:
1. Dashboard → Gráfico de barras simple
2. Ventas y Compras → Factura con flecha bidireccional
3. Inventario → Caja con productos adentro
4. Facturación SIFEN → Documento con sello QR
5. Tributario y Fiscal → Balanza
6. Contabilidad → Libro con líneas de asiento
7. Cajas → Billete/moneda
8. Préstamos → Calculadora
9. Multimoneda y Multisucursal → Dos círculos superpuestos (GS/USD)

### 2.3 Tipografía

**Actual:** Segoe UI (inferido del BRANDING.md original)

**Propuesta según branding_estrategico.md:**
- Títulos: **Plus Jakarta Sans** (Google Fonts, gratis)
- Body: **Inter** (Google Fonts, gratis)

**Implementación:**
```html
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Inter:wght@300;400;500&display=swap" rel="stylesheet">
```

```css
body { font-family: 'Inter', sans-serif; }
h1, h2, h3, h4, h5, .navbar-brand { font-family: 'Plus Jakarta Sans', sans-serif; }
```

### 2.4 Open Graph image

Crear una imagen 1200x630px para cuando alguien comparta el link en WhatsApp:

- Fondo gris claro #F5F7FA
- Logo P3 (con eslogan) centrado
- Screenshot del dashboard difuminado de fondo
- Eslogan: "ERP paraguayo. Cumplimiento real. Soporte local."

Guardar como: `/static/img/og-image.png`

### 2.5 WhatsApp flotante

El briefing lo pide pero no confirmé que exista. Agregar botón flotante bottom-right:
```html
<a href="https://wa.me/595992504620" class="whatsapp-float" target="_blank">
  <i class="bi bi-whatsapp"></i>
</a>
```
```css
.whatsapp-float {
  position: fixed;
  bottom: 24px;
  right: 24px;
  width: 56px;
  height: 56px;
  background: #25D366;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 28px;
  z-index: 9999;
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}
```

---

## 3. SEO

### 3.1 Meta tags

```html
<title>Ñande ERP — ERP paraguayo con facturación electrónica SIFEN</title>
<meta name="description" content="ERP paraguayo con facturación electrónica SIFEN, cumplimiento tributario Ley 6380 y contabilidad. Hecho en Paraguay por GuaraníSoft.">
<meta name="keywords" content="ERP Paraguay, facturación electrónica, SIFEN, contabilidad paraguaya, Ley 6380, GuaraníSoft, Ñande ERP">
```

### 3.2 Open Graph

```html
<meta property="og:title" content="Ñande ERP — ERP paraguayo. Cumplimiento real. Soporte local.">
<meta property="og:description" content="Sistema de gestión diseñado para empresas paraguayas. Cumplimiento tributario, facturación electrónica y contabilidad — todo en uno.">
<meta property="og:image" content="https://guaranisof.com/static/img/og-image.png">
<meta property="og:url" content="https://guaranisof.com">
<meta property="og:type" content="website">
```

### 3.3 Datos estructurados (Schema.org)

```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "Ñande ERP",
  "applicationCategory": "BusinessApplication",
  "operatingSystem": "Windows",
  "description": "ERP paraguayo con facturación electrónica SIFEN, cumplimiento tributario y contabilidad.",
  "publisher": {
    "@type": "Organization",
    "name": "GuaraníSoft",
    "url": "https://guaranisof.com"
  },
  "offers": {
    "@type": "Offer",
    "priceCurrency": "PYG",
    "availability": "https://schema.org/InStock"
  }
}
```

---

## 4. Prueba social

### 4.1 Testimonios

Aunque sea el primer cliente, se puede usar:

**Opción A — Si hay un cliente piloto:**
> "Antes usábamos Excel para todo. Con Ñande ERP facturamos en minutos y el inventario se actualiza solo." — [Nombre], [Empresa]

**Opción B — Si no hay clientes todavía:**
> "Desarrollado dentro de una empresa paraguaya, probado contra la legislación real: Ley 6380/2019, RG 49/14, RESIMPLE."

Usar la Opción B hasta tener el primer testimonio real. Nunca inventar testimonios.

### 4.2 Logos de cumplimiento

Mostrar badges visuales:
- "SIFEN v150"
- "Ley 6380/2019"
- "RG 49/14"
- "RESIMPLE / Marangatú"

Como pequeños badges SVG con la paleta de marca, debajo del hero o en la sección de features.

---

## 5. Orden de ejecución

| # | Tarea | Impacto | Esfuerzo |
|---|-------|---------|----------|
| 1 | Agregar screenshots del dashboard en el hero | Alto | Bajo |
| 2 | Reemplazar emojis por iconos SVG | Alto | Medio |
| 3 | Ajustar texto de SIFEN ("a medida") | Alto | Bajo |
| 4 | Cambiar stats de developer a usuario | Alto | Bajo |
| 5 | Agregar footer | Medio | Bajo |
| 6 | Cambiar tipografía a Plus Jakarta Sans + Inter | Medio | Bajo |
| 7 | Agregar Open Graph image | Medio | Medio |
| 8 | Agregar WhatsApp flotante | Medio | Bajo |
| 9 | Agregar referencia de precios ("desde") | Medio | Bajo |
| 10 | SEO meta tags + datos estructurados | Medio | Bajo |
| 11 | Badges de cumplimiento | Bajo | Medio |
| 12 | Testimonio o statement de prueba social | Bajo | Bajo |

**Prioridad 1 (hacer ya):** Items 1-4
**Prioridad 2 (esta semana):** Items 5-8
**Prioridad 3 (próxima semana):** Items 9-12

---

## 6. Notas

- Los screenshots ya están tomados (`workspace/screenshots/screenshots/`)
- Los iconos SVG hay que diseñarlos — puedo armarlos yo
- La tipografía es solo cambiar el `<link>` y el CSS
- El footer y WhatsApp flotante son HTML/CSS directo
- Para los precios, necesito que confirmes el "desde" orientativo

---

*Esta propuesta es un documento vivo. Si algo no coincide con tu visión, lo cambiamos.*
