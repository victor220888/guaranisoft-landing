# Cajas

El módulo de Cajas registra todo el movimiento de dinero de la empresa (efectivo y cuentas
bancarias) y mantiene el saldo disponible actualizado por caja.

## Panel de Cajas

1. Ir a **Cajas > Panel de Cajas**.
2. Se listan todas las cajas y cuentas bancarias con su **saldo actual**.
3. Desde aquí se puede crear una caja nueva y abrir el detalle de cada una.

## Movimientos

En **Cajas > Movimientos** se ve el historial de ingresos y egresos de todas las cajas:
cobros, pagos, ingresos manuales, egresos, extracciones, depósitos y traspasos.

- Los cobros (COBRO_VENTA, INGRESO) **suman** al saldo.
- Los pagos (PAGO_COMPRA, EGRESO) **restan** del saldo.

## Disponibilidades

**Cajas > Disponibilidades** muestra el total de dinero disponible consolidado por caja,
útil para conocer la liquidez de la empresa en un vistazo.

## Verificación de Caja

> Disponible si la empresa tiene activado el módulo **Verificación de Caja**.

En **Cajas > Verificación de Caja** se compara el saldo lógico del sistema con el conteo
físico (arqueo), para detectar diferencias.

## Cierre del día

**Cajas > Cierre del día** cierra la jornada de la caja: registra el arqueo final y deja el
saldo conciliado para el día siguiente.

## Adelantos, extracciones y depósitos

- **Extracción / Depósito**: mueve dinero entre la caja física y una cuenta bancaria.
- **Adelantos**: ver el manual de [Cobros y Pagos](cobros-pagos).
