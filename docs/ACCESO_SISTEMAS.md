# Acceso a los sistemas de GuaraníSoft

> Guía para agentes de marketing y otros colaboradores

---

## 1. Landing Page (pública)

**URL:** https://guaranisof.com

- No necesita login
- Es la página que ven los clientes
- Puede tomar capturas de: hero, features, cómo funciona, precios, formulario de contacto
- Para probar el formulario: llenar con datos de prueba y enviar — el lead se guarda en Google Sheets
- ⚠️ Esperar 30-50 segundos la primera vez (Render Free "duerme" la app si no hay tráfico)

---

## 2. ERP Ñande ERP (local)

**URL:** http://172.31.201.23:8000

### Login — Paso 1 (seleccionar empresa)
1. Abrir http://172.31.201.23:8000
2. Seleccionar empresa de prueba
3. Click "Continuar"

### Login — Paso 2 (credenciales)
- **Email:** admin@demo.com
- **Contraseña:** admin123
- **Usuario:** Administrador Demo

### Módulos para capturar
| Módulo | Qué capturar |
|--------|--------------|
| **Dashboard** | Indicadores, gráficos, tarjetas de resumen |
| **Ventas** | Lista de facturas, nueva factura |
| **Compras** | Lista de órdenes de compra |
| **Inventario** | Lista de productos, kardex |
| **Facturación SIFEN** | DTEs emitidos, estados |
| **Tributario** | Liquidadores, DDJJ |
| **Contabilidad** | Plan de cuentas, asientos |
| **Cajas** | Movimientos, arqueo |
| **Acerca de** | Info del producto, créditos |

### Para tomar capturas
- Navegador en modo incógnito (interfaz limpia)
- Resolución 1920x1080 para escritorio
- También capturar versión mobile (F12 → responsive → 375px)
- Logo y colores: morado #5B2A86 + verde #4A7C59

---

## 3. Google Sheets (leads)

**Sheet:** "Leads GuaraníSoft"
- Pestaña "Ñande ERP" — leads del formulario de la landing
- Pestaña "Ñande CRM" — para futuro producto CRM
- Acceso: Victor comparte el sheet con el email del agente

---

## 4. Branding

- **Logo completo:** `docs/logo_conceptos/P3_con_eslogan.svg`
- **Logo compacto:** en la landing `/static/img/logo-compacto.svg`
- **Paleta:** morado `#5B2A86`, verde `#4A7C59`, gris `#F5F7FA`
- **Eslogan:** "ERP paraguayo. Cumplimiento real. Soporte local."

---

## 5. Datos para marketing

**Stats reales del ERP:**
- 96 tablas de datos
- 350+ endpoints
- 7 tipos de DTE SIFEN
- Cumplimiento: Ley 6380/2019, RG 49/14, RESIMPLE, SIFEN v150

**Contacto:**
- Web: guaranisof.com
- Email: ventas@guaranisof.com, soporte@guaranisof.com
- WhatsApp: +595 992 504 620
- LinkedIn: https://www.linkedin.com/in/victor-roman-226bb155/

---

*Documentado el 2026-06-18.*
