# Estructura del Proyecto ERP Paraguay

> **Fuente canónica del mapa estructural** — referenciada desde `CLAUDE.md`
> Última actualización: 2026-06-14

---

## Raíz (`~/erp-system/`)

```
erp-system/
├── .claude/                          # Config Claude Code: CLAUDE.md (global negocio+metodología),
│                                     #   MANUAL_DESARROLLADOR.md (alta cliente dev-side + migraciones),
│                                     #   commands/ (slash commands), settings.local.json
├── .env                              # Variables de entorno (secrets, DB, etc.)
├── .env.example                      # Template de variables de entorno
├── .gitignore                        # Archivos/carpetas excluidos del repo
├── .coverage                         # Cobertura de tests (pytest)
├── alembic/                          # Migraciones de base de datos (Alembic)
├── alembic.ini                       # Configuración de Alembic
├── db/                               # Dumps de base de datos
├── docs/                             # Documentación del proyecto
├── fuentes_legales/                  # Normativa fiscal/legal de Paraguay
├── modelo_datos/                     # DER y SQL del modelo de datos
├── pyproject.toml                    # Configuración del proyecto (deps, ruff, etc.)
├── requirements.txt                  # Dependencias Python
├── scripts/                          # Scripts utilitarios (seed, fixes, tests manuales)
├── sql/                              # SQL manual (ejecuciones fuera de migraciones)
├── src/                              # ⭐ Código fuente de la aplicación
├── tests/                            # Tests automatizados
├── .venv/                            # Entorno virtual Python (activo — el que usa el proyecto)
├── AGENTS.md                         # Orquestación entre agentes de IA (auto-carga en OpenCode)
├── ARCHITECTURE.md                   # Arquitectura del sistema
├── CLAUDE.md                         # Contexto del proyecto ERP — leer primero (source of truth)
├── README.md                         # Documento principal del proyecto
```

---

## `alembic/` — Migraciones de BD

```
alembic/
├── env.py                            # Configuración del entorno Alembic
├── script.py.mako                    # Template de migración
└── versions/                         # Migraciones versionadas — ver tabla "Migraciones Alembic" abajo
```

---

## `db/` — Dumps de base de datos

```
db/
├── Dump20260523.sql                  # Dump DB del 2026-05-23
└── Dump20260529.sql                  # Dump DB del 2026-05-29
```

---

## `docs/` — Documentación del proyecto

Documentación técnica activa por área (motor contable, préstamos, SIFEN, reportes
SET, etc.) + `CHANGELOG.md` (bitácora) + `STRUCTURE.md` (este archivo). Planes
completados, handoffs de sesión y notas efímeras se archivan en `docs/archivo/`.
`docs/auditoria_glm5_turbo/` y `docs/backups/` contienen material de auditorías/
correcciones puntuales. Para el listado completo: `ls docs/`.

---

## `fuentes_legales/` — Normativa fiscal/legal de Paraguay

```
fuentes_legales/
├── Contexto normativo para modelado ERP tributario Paraguay.md
├── Especificaciones_Técnicas_para_registro_de_comprobantes_en_Marangatu.pdf
├── Guia Paso a Paso - Consulta de comprobantes registrados.pdf
├── Guía de Mejores Prácticas para la Gestión del Envío de DE.pdf
├── LEY N° 6.380.txt
├── Ley 6380-2019- modernización y simplificación sel sistema tributario.md
├── Ley 6380-2019- modernización..._parte1.pdf
├── Ley 6380-2019- modernización..._parte2.pdf
├── Manual Técnico Versión 150.pdf
├── ley-125_1991-establece-el-nuevo-rgimen-tributario.pdf
├── marangatu_registro_comprobantes.md
├── mesicic3_pry_ley2421.pdf
├── RG49_14_Anexos.xls                 # RG 49/14 SET — 6 pestañas: Anexo 1 BG, 2 ER, 3 Flujo Efectivo, 4 Cambios P.Neto, 5 Notas, 6 Revalúo
└── RG49_14_Referencia.md              # Texto legal completo: artículos, estructura de los 6 anexos, normas modificatorias (incl. RG 49/2026)
```

---

## `modelo_datos/` — DER y SQL del modelo de datos

```
modelo_datos/
├── DER_00_INDICE.md                   # Índice general del DER
├── DER_01_CONTEXTO_PROYECTO.md        # Contexto y alcance del proyecto
├── DER_02_MAESTROS.md                 # DER — Módulo Maestros
├── DER_03_COMERCIAL_INVENTARIO.md     # DER — Módulo Comercial e Inventario
├── DER_04_TRIBUTARIO_FISCAL.md        # DER — Módulo Tributario/Fiscal
├── DER_05_SIFEN.md                    # DER — Módulo SIFEN
├── DER_06_CONTABILIDAD.md             # DER — Módulo Contabilidad
├── DER_ERP_Paraguay_Documentacion_v5.9.html  # Documentación visual del DER v5.10
├── DER_ERP_Paraguay_SQL_v5.11.sql      # SQL completo del DER v5.11 (95 tablas + 13 triggers)
├── DER_REFERENCIA_RAPIDA.md           # Referencia rápida (nombre, propósito, PK, FKs)
├── SQL_DBA_permisos_granulares.sql    # SQL de permisos granulares para DBA
├── seed_normas_legales_v1.sql         # Seed de normas legales
└── verificar_compra_contado.sql       # Script de verificación compra contado
```

---

## `scripts/` — Scripts utilitarios

```
scripts/
├── create_superuser.py                # Crear usuario superadmin
├── fix_movimientos_kardex.py          # Fix de movimientos en kardex
├── fix_stock_compras.py               # Fix de stock en compras
├── reset_compras_kardex_stock.py      # Reset de compras/kardex/stock
├── run_create_fase2.py                # Runner de creación fase 2
├── seed.py                            # Seed principal de datos
├── migrate_plan_cuentas_set.py        # Migra plan X.X.X → X.XX.XX.XX Balance General SET
├── migrate_plan_cuentas_er.py         # Migra secciones 4-19 al Estado de Resultados SET
├── seed_plan_cuenta.py                # Seed del plan de cuentas (obsoleto, ver seed_plan.py)
├── seed_tributario.py                 # Seed de datos tributarios
├── test_flujo_compra_venta.py         # Test manual flujo compra → venta
└── test_operativo.py                  # Test operativo general
```

---

## `sql/` — SQL manual

```
sql/
└── manual/
    └── 20260528_activos_fiscales_v2.sql   # SQL manual activos fiscales v2
```

---

## `src/` — Código fuente de la aplicación

> Solo se listan carpetas contenedoras de `.py`, no archivos individuales (excepto `main.py` y `notas_de_Victor.md`).

```
src/
├── main.py                            # Entry point de la aplicación (FastAPI)
├── notas_de_Victor.md                 # Notas del owner sobre el código
│
├── api/                               # Capa de API REST (endpoints)
│   └── v1/                            # API v1
│
├── core/                              # Configuración y seguridad central
│
├── models/                            # Modelos SQLAlchemy (ORM)
│   ├── contabilidad/                  # Asiento, plan_cuenta, ejercicio, cierre, etc.
│   ├── marangatu/                     # Configuración Marangatú
│   ├── sifen/                         # Timbrado, documento_electronico, DE, logs
│   └── tributario/                    # (Vacío — contenido en services)
│
├── schemas/                           # Schemas Pydantic (validación/serialización)
│
├── services/                          # Lógica de negocio (service layer)
│   ├── contabilidad/                  # Asiento, generador_asientos, plan_cuenta,
│   │                                  #   cierre, cuenta_corriente, reportes, seed_plan
│   ├── marangatu/                     # Configuración Marangatú
│   ├── sifen/                         # Firma_digital, XML, envío lotes, timbrado,
│   │                                  #   QR, consulta CDC, codificaciones, eventos
│   └── tributario/                    # Liquidadores (IDU/IRE/IRP), libro_iva,
│                                      #   motor_reglas, retención, vigencia, seeds
│
├── static/                            # Archivos estáticos
│   ├── css/                           # custom.css, print.css
│   ├── img/                           # (vacío — .gitkeep)
│   └── js/                            # app.js
│
├── templates/                         # Plantillas Jinja2 (HTMX + Alpine.js)
│   ├── base.html                      # Layout base principal
│   ├── base_print.html                # Layout base para impresión
│   ├── base_public.html               # Layout base público
│   ├── components/                    # Componentes reutilizables (modal, table, form, toast, pagination, confirm_delete, document-info)
│   ├── errors/                        # Páginas de error
│   ├── partials/                      # navbar.html, sidebar.html
│   └── pages/                         # Páginas del sistema (ver detalle abajo)
│       ├── auth/                      # Login
│       ├── cajas/                     # Gestión de cajas
│       ├── categorias/                # Categorías de productos
│       ├── cobros/                    # Cobros/cuotas
│       ├── compras/                   # Compras
│       ├── comprobante/               # Comprobantes (form, detalle, index, rápido)
│       ├── config/                    # Configuración (períodos)
│       ├── contabilidad/              # Contabilidad (asientos, plan_cuenta, ejercicios, cierre, etc.)
│       ├── dashboard/                 # Dashboard principal
│       ├── depositos/                 # Depósitos
│       ├── empresas/                  # Empresas
│       ├── inventory/                 # Inventario (ajustes, traslados, verificaciones, movimientos) ⚠️ en inglés
│       ├── lineas_negocio/            # Líneas de negocio
│       ├── marcas/                    # Marcas
│       ├── onboarding/                # Onboarding
│       ├── prestamos/                 # Préstamos
│       ├── productos/                 # Productos (CRUD + precios masivos)
│       ├── puntos_emision/            # Puntos de emisión
│       ├── proveedores/               # Proveedores
│       ├── reportes/                  # Reportes comerciales (ventas, compras, stock, margen)
│       ├── reports/                   # Reportes contables (balance, mayor, libro diario, IVA, comprobante) ⚠️ en inglés
│       ├── sifen/                     # Configuración e índice SIFEN
│       ├── sucursales/                # Sucursales
│       ├── terceros/                  # Terceros (clientes/proveedores)
│       ├── timbrado/                  # Timbrados
│       ├── tributario/                # Módulo tributario completo (activos fiscales, escalas, retenciones, etc.)
│       ├── usuarios/                  # Gestión de usuarios y permisos
│       ├── ventas/                    # Ventas
│       └── wip.html                   # Work in progress (placeholder)
│
└── utils/                             # Utilidades generales
```

---

## `tests/` — Tests automatizados

```
tests/
├── __init__.py
├── conftest.py                        # Fixtures compartidas
├── factories.py                       # Factories de datos de prueba
│
├── api/                               # Tests de endpoints API
│   ├── test_auth.py                   # Tests de autenticación
│   └── test_customers.py              # Tests de clientes
│
├── security/                          # Tests de seguridad
│   ├── conftest.py                    # Fixtures de seguridad
│   ├── test_aislamiento_tenant.py     # Aislamiento multi-tenant
│   ├── test_idor_getters.py           # Protección IDOR en getters
│   └── test_rest_endpoints.py         # Tests de endpoints REST
│
└── services/                          # Tests de la capa de servicios
    ├── test_cobros.py                 # Tests de cobros
    ├── test_marangatu_export.py       # Tests de exportación Marangatú
    ├── test_sale.py                   # Tests de ventas
    ├── contabilidad/                  # Tests de contabilidad
    │   ├── test_cierre.py             # Tests de cierre contable
    │   ├── test_cuenta_corriente.py   # Tests de cuentas corrientes
    │   ├── test_generador_asientos.py # Tests del generador de asientos
    │   └── test_reporte_contable.py   # Tests de reportes contables
    └── tributario/                    # Tests de tributario
        ├── test_liquidador_idu.py     # Tests liquidador IDU
        ├── test_liquidador_ire.py     # Tests liquidador IRE
        ├── test_motor_reglas.py       # Tests motor de reglas
        └── test_seed_tributario.py    # Tests seed tributario
```

---

## Inventario de la aplicación

> Extraído de `CLAUDE.md` — este es el hogar canónico del inventario detallado.

### Modelos ORM (95 total)

> Conteo autoritativo: **95 tablas** (`grep -rh __tablename__ src/models | wc -l`; en 39 archivos de modelo). Subcarpetas: `tributario/` 21, `contabilidad/` 12, `sifen/` 7, `marangatu/` 1; raíz 54. El desglose por grupo de abajo es **indicativo** — varios grupos crecieron desde este listado y la suma de nombres no llega a 95.

| Grupo | Cant. | Modelos |
|-------|-------|---------|
| Maestros | 20 | Moneda, UnidadMedida, Impuesto, RegimenTributario, Rol, Usuario, UsuarioEmpresa, Empresa, Sucursal, PuntoEmision, Deposito, Marca, LineaNegocio, Tercero, TerceroEmpresa, CuentaBancariaTercero, TerceroRegimenHistorial, CategoriaProducto, Producto, LoteProducto |
| Inventario | 9 | StockDeposito, MovimientoStock, CostoValoracion, LogCambioCosto, AjusteStock, VerificacionStock, VerificacionStockDetalle, TrasladoCab, TrasladoDet |
| Comercial | 11 | TipoComprobante, CondicionVenta, MedioPago, MotivoNota, TipoCambio, Timbrado, Comprobante, ComprobanteItem, ComprobanteCondicion, ComprobanteEstadoLog, CuentaBancariaTercero |
| Caja/Períodos | 4 | Caja, MovimientoCaja, CobroDistribucion, CierrePeriodo |
| SIFEN | 7 | DocumentoElectronico, EventoSifen, InutilizacionSifen, LoteSifen, LoteSifenDetalle, SifenLog, ConfiguracionSifen |
| Tributario | 18 | NormaLegal, ArticuloNormativo, TasaImpuesto, ResimpleEscala, TipoRetencion, AjusteFiscal, PerdidaFiscal, DeclaracionJurada, PagoImpuesto, RetencionPercepcion, DistribucionUtilidad, DistribucionUtilidadDetalle, ActivoFiscal, RegistroFiscal, CambioRegimen, MovimientoDepreciacion, ParteRelacionada, OperacionParteRelacionada |
| Contabilidad | 11 | PlanCuenta, CentroCosto, EjercicioFiscal, AsientoContable, AsientoLinea, SecuenciaAsiento, PlantillaAsiento, PlantillaAsientoLinea, CuentaConceptoMap, CuentaCorriente, CierreEjercicio |
| Marangatu | 1 | ConfiguracionMarangatu |
| Préstamos | 1 | PrestamoAmortizacion |
| Permisos | 3 | Permiso (catálogo global), RolPermiso (defaults por rol), UsuarioEmpresaPermiso (overrides GRANT/REVOKE por usuario-empresa) |

**Ubicación:** `src/models/` — raíz para modelos generales; subcarpetas `contabilidad/`, `marangatu/`, `sifen/`, `tributario/` para los especializados.

### Schemas Pydantic (17 archivos)

usuario, empresa, sucursal, deposito, tercero, categoria, producto, marca, linea_negocio, comprobante, inventario, sifen, caja, cobros, tributario, contabilidad, marangatu

**Ubicación:** `src/schemas/`

### Services (62 archivos: raíz 32, contabilidad 12, tributario 9, sifen 8, marangatu 1 + lógica embebida)

| Área | Services |
|------|---------|
| Maestros | empresa, sucursal, deposito, tercero, categoria, producto, marca, linea_negocio, user, catalogo_comercial |
| Comercial/Inventario | comprobante (~910 líneas — CPP + kardex + SIFEN), costeo (504 líneas), inventario (351), traslado (265), verificacion (244), periodo (198), caja (91), cobros (138), timbrado (132) |
| Reportes | reporte (PDF — comprobante A4 + ticket), reportes_comerciales (ventas, compras, stock, margen, cuentas) |
| SIFEN | codificaciones, generador_xml, firma_digital, generador_qr, envio_lotes, consulta_cdc, eventos, inutilizacion (~3,500 líneas totales) |
| Tributario | vigencia (2,000+ líneas), liquidador_ire, liquidador_idu, liquidador_irp, motor_reglas, retencion, libro_iva, seed_activos_fiscales, seed_tributario |
| Contabilidad | plan_cuenta, centro_costo, ejercicio_fiscal, secuencia_asiento, asiento, plantilla, concepto_map, cuenta_corriente, generador_asientos, cierre, reporte_contable (+ flujo_efectivo, cambios_patrimonio, notas_ef, cuadro_revaluo, inventario_balances), seed_plan (12 services)
| Contabilidad (embebido) | libro_iva dentro de reporte_contable, verificacion_caja dentro de caja — no archivos independientes |
| Marangatu | marangatu_export, marangatu/configuracion |
| Préstamos | _(lógica en paginas.py)_ — 4 sistemas amortización, preview, PDF, edición (no archivo service independiente) |
| Setup | seed_empresa, seed_permisos, seed_activos_fiscales
| Docker | _(Dockerfile, docker-compose.yml, Makefile, entrypoint.sh, /health)_ |
| Permisos | permisos — `get_permisos_efectivos()`, `aplicar_override()`, `eliminar_override()`, `restaurar_defaults()`, `listar_permisos_con_estado()` |

**Ubicación:** `src/services/` — raíz para services generales; subcarpetas `contabilidad/`, `marangatu/`, `sifen/`, `tributario/` para los especializados.

### Rutas HTMX principales

| Área | Rutas |
|------|-------|
| Auth | `/login`, `/login/acceder`, `/onboarding/nueva` |
| Maestros | empresas, sucursales, depósitos, terceros, categorías, productos, marcas, líneas negocio, puntos emisión |
| Comercial | comprobantes (index/form/detalle), compras (index/form), ventas (index/form), timbrado (index/form) |
| Carga rápida | `/ventas/rapido`, `/compras/rapido` — formulario dos paneles Alpine.js, búsqueda AJAX |
| AJAX search | `/api/productos/buscar`, `/api/productos/barcode`, `/api/terceros/buscar` |
| Inventario | stock, movimientos, ajustes (CRUD), traslados (CRUD), verificaciones (CRUD) |
| Caja | cajas (CRUD), cobros (index/pagar), disponibilidad, movimientos, aporte-inicial, verificación |
| Períodos | `/config/periodos` (cierre/reapertura) |
| Reportes | compras por período/proveedor, ventas netas, stock valorizado, margen bruto, inventario valorizado, Marangatu |
| SIFEN | dashboard con tabs Documentos/Lotes/Logs |
| Tributario | 11 entidades (~70 handlers) + `/tributario/marangatu` |
| Contabilidad | plan de cuentas, ejercicios, centros costo, asientos, plantillas, conceptos, cuentas corrientes, cierre + 6 reportes PDF + 5 CSV + flujo efectivo (Anexo 3) + cambios patrimonio (Anexo 4) + notas EF (Anexo 5) + cuadro revalúo (Anexo 6) + inventario/balances + libro IVA (excluir/restaurar) |
| Préstamos | `/prestamos` (lista), `/prestamos/nuevo` (form con preview amortización), `/prestamos/{id}/pdf` (cuadro amortización PDF) |
| Permisos | `/usuarios` (index), `/usuarios/{id}/empresas` (accesos + cambio rol), `/usuarios/{id}/permisos?empresa_id=X` (checkboxes por módulo) |

**API REST adicional:** `marangatu.py` (prefijo `/marangatu`), `contabilidad.py` (17 endpoints), `sifen.py` (14 endpoints), `tributario.py` (21 endpoints)

### Templates (180 archivos)

> Conteo autoritativo: **180** (`find src/templates -name '*.html' | wc -l`). El desglose de abajo es indicativo. Incluye:
- 9 PDF templates (WeasyPrint): libro diario, balance sumas/saldos, mayor cuenta, estado resultados, balance general, flujo efectivo, cambios patrimonio, cuadro revalúo, comprobante A4, comprobante ticket, cuadro amortización préstamo
- 11 páginas inventario, 4 páginas comprobante (form, form_rapido, index, detalle), 25 páginas tributario, 18 páginas contabilidad
- 2 páginas préstamos (index, form con Alpine.js y preview amortización en tiempo real)
- 3 páginas permisos (usuarios/index, usuarios/empresas, usuarios/permisos)
- `reportes_contables/flujo_efectivo.html` — Flujo de Efectivo Anexo 3 SET (L1..L20, cuadre L19+L18=L20)
- `reportes_contables/cambios_patrimonio.html` — Cambios del Patrimonio Neto Anexo 4 SET (A4 landscape, DEBE/HABER separados en 3.03.02)
- `reportes_contables/notas_ef.html` — Notas a los Estados Financieros Anexo 5 SET (secciones auto + editables)
- `reportes_contables/cuadro_revaluo.html` — Cuadro Revalúo Anexo 6 SET (16 columnas por ActivoFiscal)
- `reportes_contables/inventario_balances.html` — Libro Inventarios y Balances (14 secciones SET)
- `cajas/aporte_inicial.html` — Aporte inicial / Cuenta particular propietario

### Migraciones Alembic (34 versiones — current: `20260612_arqueo_caja`)

| # | Migración | Descripción |
|---|-----------|-------------|
| 1 | `20260426_e51b42bd1350_baseline_der_v52` | Baseline — tablas DER v5.2 ya existían en BD |
| 2 | `20260426_fase1_maestros_orm` | Fase 1 — Maestros ORM |
| 3 | `20260427_add_empresa_codigo` | Agregar código a empresa |
| 4 | `20260427_der_v54_marca_linea_negocio` | DER v5.4 — marca y línea de negocio |
| 5 | `20260429_a84a08cc72ec_add_medio_pago` | Medio de pago en comprobante_condicion |
| 6 | `20260429_c3f7a2b84d91_align_caja_der_v55` | Alinear caja con DER v5.5 |
| 7 | `20260430_snapshot_v57` | Snapshot DER v5.7 |
| 8 | `20260504_b2c3d4e5f6a7_configuracion_sifen` | Configuración SIFEN |
| 9 | `20260504_c0d1e2f3a4b5_modulo_tributario_fase5` | Módulo tributario fase 5 |
| 10 | `20260505_d1e2f3a4b5c6_contabilidad_fase6` | Contabilidad fase 6 |
| 11 | `20260506_add_medio_pago_condicion` | Medio de pago en condición |
| 12 | `20260506_fase7_liquidacion` | Liquidación fase 7 |
| 13 | `20260509_marangatu_configuracion` | Configuración Marangatú |
| 14 | `20260512_add_nota_credito_debito_enum` | Enum nota crédito/débito |
| 15 | `20260514_caja_tipos_tarjeta` | Tipos de tarjeta en caja |
| 16 | `20260516_autofactura_ticket_boleta` | Autofactura, ticket, boleta |
| 17 | `20260520_prestamo_enums` | Enums de préstamo |
| 18 | `20260521_prestamo_v59` | Préstamos DER v5.10 |
| 19 | `20260521b_prestamo_sistemas` | Préstamo sistemas (DIAS_REALES, PERSONALIZADO) |
| 20 | `20260521c_permisos_granulares` | Permisos granulares DER v5.10 |
| 21 | `20260522_anulacion_enums` | Enums de anulación (stamped) |
| 22 | `20260522b_uk_comprobante_con_estado` | 3 UKs con estado (stamped) |
| 23 | `20260522c_cta_cte_sucursal_not_null` | sucursal_id NOT NULL (current) |
| 24 | `20260522d_prestamo_estados_cancelado` | Estado cancelado en préstamo |
| 25 | `20260528_verificacion_caja` | Verificación de caja |
| 26 | `20260528b_activos_fiscales_v2` | Activos fiscales v2 |
| 27 | `20260529_adelantos_extraccion` | Adelantos + extracción/depósito |
| 28 | `20260603_nota_ef` | Notas a los EE.FF. (Anexo 5) |
| 29 | `20260604_cuota_monto_pagado` | `monto_pagado` en cuota |
| 30 | `20260605_empresa_feature_config` | Tablas empresa_feature / config_empresa |
| 31 | `20260605b_instalacion` | Licencia singleton de instalación |
| 32 | `20260610_cobro_distribucion_anulacion` | Anulación en cobro_distribucion |
| 33 | `20260610b_movcaja_reversa` | `movimiento_caja.reversa_de_id` |
| 34 | `20260612_arqueo_caja` | Arqueo de caja (current) |

### Tests (329 funciones `test_` en 30 archivos)

> Conteo de funciones definidas (`grep -rh "def test_" tests/ | wc -l`), no de "pasando" — en este entorno pytest no corre limpio por el `DATABASE_URL`. Por carpeta:

| Carpeta | Funciones |
|---------|-----------|
| `tests/services/` (raíz) | 173 |
| `tests/services/contabilidad/` | 69 |
| `tests/services/tributario/` | 24 |
| `tests/security/` | 27 |
| `tests/consultoria/` | 36 |

---

## Hallazgos de limpieza

`venv/` redundante, carpetas de templates vacías en inglés y scripts `.py`
sueltos en raíz ya **no existen** (resuelto). `docs/auditoria_glm5_turbo/` ya
no tiene `.py` (movidos). Pendiente: ~22 archivos `.Zone.Identifier` (basura
NTFS en `fuentes_legales/` y `modelo_datos/`, eliminar cuando se toque esa
carpeta) y los renombres `.py` inglés→español (models/services `category`,
`product`, `inventory`, `role`, `user` y derivados) — detalle completo y
procedimiento paso a paso en `TAREA_limpieza_estructura.md`.
