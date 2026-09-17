# Menú y Navegación

> Última actualización: 2026-06-03
> Fuente de verdad de la **arquitectura de información** de la navegación del ERP.

El sistema tiene **dos menús** que deben mantenerse coherentes entre sí:

| Menú | Archivo | Rol |
|------|---------|-----|
| **Sidebar** (lateral) | `src/templates/partials/sidebar.html` | Navegación completa, siempre visible. **Fuente de verdad de la IA.** |
| **Home** (tarjetas) | `src/templates/pages/home.html` | Landing post-login (`/home`). Reflejo amigable y agrupado del sidebar. |

## Regla de oro: paridad home ↔ sidebar

**Todo destino del sidebar debe ser alcanzable desde una tarjeta del home.** Si agregás una página
al sidebar, agregala también al `modules` de `home.html` (y viceversa). Un menú nunca debe tener un
destino que el otro no tenga.

**Excepciones deliberadas** (paridad a nivel *página*, no de cada deep-link):
- Filtros / sub-acciones (ej. `/cobros?tipo=ADELANTO_*`, "Nuevo Adelanto") → accesibles desde su
  página padre, no se listan como tarjeta.
- Sub-config (ej. Activos Fiscales → Tipos / Métodos Deprec.) → accesible desde su página padre.
- **Desarrollo / Test Runner** → solo sidebar, bajo `{% if DEBUG %}`. No es módulo de negocio.

Verificación rápida de paridad (no debe faltar nada):

```bash
.venv/bin/python -c "
import re
home = open('src/templates/pages/home.html').read()
side = open('src/templates/partials/sidebar.html').read()
home_urls = set(re.findall(r'\(\"(/[^\"?]+)\"', home))
side_urls = set(re.findall(r'href=\"(/[^\"?]+)\"', side))
ignore = {'/admin/tests/','/tributario/activos-fiscales/tipos','/tributario/activos-fiscales/metodos','/cobros/adelanto/nuevo','/home','/dashboard'}
print('Faltan en home:', sorted(side_urls - home_urls - ignore) or 'NINGUNO ✅')
"
```

## Estructura del Home (8 tarjetas)

Orden: flujo diario primero, analítica y administración al final.

| # | Tarjeta | Color | Grupos |
|---|---------|-------|--------|
| 1 | **Operaciones** | blue | Ventas · Compras · Comprobantes y Cobranzas |
| 2 | **Cajas** | green | Cajas (panel, movimientos, disponibilidades, verificación) |
| 3 | **Inventario** | teal | Stock (resumen, kardex, ajustes, traslados) |
| 4 | **Catálogos** | orange | Productos · Terceros · Clasificaciones |
| 5 | **Fiscal y Tributario** | red | IVA · Renta y DDJJ · Retenciones · Ajustes y Activos · Marangatú |
| 6 | **Contabilidad** | purple | Asientos y Plan · Ejercicios · Saldos y Reportes |
| 7 | **Reportes** | pink | Reportes del Sistema |
| 8 | **Configuración** | gray | Empresa · Parámetros Fiscales · Sistema |

### Criterio de agrupación (por naturaleza)

- **Operativo vs configuración**: lo que el usuario *ejecuta* a diario (Libro IVA, Liquidación,
  DDJJ…) va en la tarjeta **Fiscal y Tributario**; lo que se *parametriza una vez* (Tasas, Escalas,
  Normas, Tipos de Retención) va en **Configuración → Parámetros Fiscales**. **Los parámetros
  fiscales viven en un solo lugar** para evitar el "¿en qué tarjeta busco?".
- **Cajas ≠ Inventario**: efectivo y stock son dominios distintos → tarjetas separadas.
- **Nombres = su contenido**: el grupo "Ejercicios" de Contabilidad agrupa Ejercicios Fiscales,
  Centros de Costo y Cierre; no se llama "Períodos" para no chocar con el ítem Períodos
  (`/config/periodos`) de Configuración.

## Detalle técnico

### Home — `home.html`
- La estructura vive en la variable Jinja `modules` (lista de dicts). Cada tarjeta:
  `{id, icon, color, title, desc, groups[]}`; cada grupo: `{label, icon, links[]}`; cada link es la
  tupla `("/ruta", "bi-icono", "Etiqueta")`.
- Render: tarjetas con Bootstrap + popup modal Alpine.js (`x-data="{ selectedId: null }"`). El badge
  de cada tarjeta cuenta los links automáticamente (`groups|map('links')|map('length')|sum`).
- **Tarjeta de destino único**: si la tarjeta tiene un solo destino, agregar `"href": "/ruta"` y
  `"groups": []`. Se renderiza como `<a>` que navega directo (sin popup, sin badge) y queda excluida
  del loop del modal (`{% for mod in modules if not mod.href %}`). Ej.: la tarjeta **Reportes**.
- **Colores disponibles** (`.home-card-icon.<color>` en `custom.css`): blue, green, orange, red,
  purple, gray, teal, pink. Agregar una tarjeta nueva con color nuevo requiere su clase CSS.

### Sidebar — `sidebar.html`
- **Riel de iconos que se expande on-hover (desktop ≥769px):** por defecto el sidebar es un riel
  angosto (72px) que muestra **solo iconos** — los 3 accesos rápidos + un icono por sección (mismo
  `bi-*` que la tarjeta del home correspondiente). Al pasar el mouse se expande a 264px (overlay,
  con sombra) y aparecen los textos, chevrons y los items de cada sección. **No refluye el contenido**:
  el `<main>` reserva 72px de margen izquierdo y la expansión se superpone.
- Implementación CSS en `custom.css`, bloque `@media (min-width: 769px)`:
  - Riel = estado `#sidebar:not(:hover)` → oculta `.nav-text`, `.sidebar-section-text`,
    `.sidebar-section-chevron` y las listas `.sidebar-collapse-section`; centra los iconos.
  - Expandido = `#sidebar:hover` → ancho 264px; las secciones colapsables respetan su estado
    Bootstrap (`.show` visible).
  - Cada cabecera de sección lleva `<i class="... sidebar-section-icon">` + `<span class="sidebar-section-text">`;
    los accesos rápidos llevan `<span class="nav-text">` para poder ocultar el texto en modo riel.
- **Móvil (≤768px):** sin cambios — drawer deslizable existente (`transform: translateX`).
- Secciones colapsables (Bootstrap Collapse). "Operaciones" abierta por defecto; el resto cerradas.
- El item activo se resalta comparando `request.url.path` con `path.startswith('/ruta')`.
- La sección **Desarrollo** (Test Runner) está envuelta en `{% if DEBUG %}` — `DEBUG` se expone como
  global de Jinja2 en `paginas.py` (`templates.env.globals["DEBUG"] = settings.DEBUG`).

### Routing
- `/` , post-login y callbacks de auth redirigen a `/home` (`paginas.py`, `auth.py`).
- Handler: `GET /home` → `home_page` en `src/api/v1/paginas.py` (auth por cookie, patrón de páginas).
