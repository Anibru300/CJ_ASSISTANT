# Core / Scheduler

## Propósito

Programación y ejecución de tareas recurrentes en CJ_OS.

## Responsabilidades

- Ejecutar tareas periódicas: reportes diarios, respaldos, sincronizaciones, alertas.
- Desencadenar eventos en el Event Bus para que n8n o los agentes los procesen.
- Mantener un registro de ejecuciones, fallos y reintentos.
- No contener lógica de negocio; solo orquesta la invocación de tareas.

## Ejemplos de tareas futuras

- Resumen diario para Carlos.
- Sincronización de Excel de almacén.
- Backup automático de PostgreSQL y workspace.
- Revisión de stock mínimo.

## Estado

- Fase M1.2.5: estructura y documentación listas.
