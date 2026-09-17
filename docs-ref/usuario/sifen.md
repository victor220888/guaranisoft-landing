# Facturación Electrónica (SIFEN)

> Disponible si la empresa tiene activado el módulo **SIFEN**.

SIFEN es el sistema de facturación electrónica de la SET. Este módulo prepara, firma y envía
los documentos electrónicos (DE) y consulta su estado.

## Configuración inicial

1. Ir a **Configuración > SIFEN**.
2. Cargar el **certificado digital** y los parámetros de conexión.
3. Verificar el **timbrado electrónico** habilitado por DNIT.

> La configuración de credenciales requiere el permiso **Configurar credenciales SIFEN**.

## Emisión de documentos electrónicos

1. Al crear una factura (ver [Facturación](facturacion)), si la empresa opera con SIFEN el
   comprobante se prepara como documento electrónico.
2. El sistema genera el **CDC** (Código de Control) y el **KuDE** (representación gráfica).
3. El documento se firma y se envía al servidor de la SET.

## Estados de un documento

- **Pendiente** — generado, aún no enviado.
- **Enviado / Aprobado** — aceptado por la SET.
- **Rechazado** — la SET lo rechazó; revisar el motivo y reemitir.

## Notas

- Los tipos Autofactura, Boleta y Ticket tienen un tratamiento especial de IVA en la
  exportación a Marangatú.
- Ante errores de conexión, verificar certificado, fecha del sistema y disponibilidad del
  servidor de la SET.
