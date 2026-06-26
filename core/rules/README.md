# Core / Rules

## Propósito

Definir y aplicar las reglas de negocio de CJ_OS.

## Responsabilidades

- Validar permisos de usuarios antes de ejecutar acciones.
- Aplicar límites, políticas y restricciones operativas.
- Garantizar que solo usuarios autorizados realicen ciertas acciones.
- Bloquear operaciones que violen reglas críticas.
- Proveer trazabilidad de qué regla se aplicó en cada decisión.

## Pregunta que responde

> **¿Qué está permitido hacer?**

## Ejemplo

- "Solo el encargado de almacén puede autorizar salidas."
- "Las órdenes de compra mayores a $50,000 requieren aprobación de Carlos."

## Fuentes esperadas

- PostgreSQL para reglas estructuradas.
- `config/` para reglas por ambiente.

## Estado

- Fase M2.1: estructura y documentación listas.
