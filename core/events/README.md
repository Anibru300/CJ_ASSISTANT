# Core / Events

## Propósito

Event Bus / cola central de eventos de CJ_OS.

## Responsabilidades

- Recibir eventos desde conectores (WhatsApp, Outlook, etc.) y desde el scheduler.
- Encolar eventos en Redis o en el medio que se defina.
- Distribuir eventos a los consumidores correspondientes (n8n, agentes, módulos).
- Garantizar trazabilidad de cada evento desde su origen hasta su resolución.

## Tipos de eventos esperados

- `message.received` — Mensaje entrante.
- `message.processed` — Mensaje procesado.
- `task.scheduled` — Tarea programada.
- `agent.invoked` — Agente invocado.
- `connector.sync` — Sincronización de conector.
- `error.raised` — Error registrado.

## Estado

- Fase M1.2.5: estructura y documentación listas.
