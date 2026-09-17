# Préstamos

> Disponible si la empresa tiene activado el módulo **Préstamos**.

Permite registrar préstamos **recibidos** (la empresa toma un préstamo) y **otorgados**
(la empresa presta dinero), con su plan de cuotas, intereses y seguimiento de pagos.

## Crear un préstamo

1. Ir a **Operaciones > Préstamos**.
2. Hacer clic en **Nuevo Préstamo**.
3. Seleccionar el **tipo** (Recibido u Otorgado) y la **contraparte** (tercero).
4. Ingresar **monto**, **tasa de interés**, **plazo** y **fecha de inicio**.
5. Guardar. El sistema genera el **plan de amortización** (cuotas con capital + interés).

## Plan de amortización

Cada cuota se descompone en **capital** e **interés**. En la cuenta corriente del tercero
solo se descuenta el **capital**; el interés se registra como gasto/ingreso.

## Cobrar o pagar una cuota

1. Abrir el préstamo y ubicar la cuota pendiente.
2. Hacer clic en **Pagar / Cobrar cuota**.
3. Seleccionar la **caja** y confirmar el monto.

El movimiento genera automáticamente el asiento contable y actualiza el saldo de la caja.

## Anular el pago de una cuota

Desde el detalle del comprobante del préstamo, en la tabla de pagos, usar **Anular** sobre
el pago a revertir. Se restaura el saldo de la cuota y se reversa el asiento y el movimiento
de caja. Ver también [Cobros y Pagos](cobros-pagos).
