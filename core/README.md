# Core de CJ_OS

El `core/` es el cerebro del sistema. Contiene los componentes transversales que orquestan, gobiernan y dan soporte a todos los dominios funcionales, agentes de IA, conectores y flujos de automatización.

## Principio arquitectónico

> **n8n es el orquestador. CJ_OS es el cerebro.**

El Core no contiene lógica de negocio específica de ningún dominio. Su responsabilidad es:

- Recibir, encolar y distribuir eventos.
- Gestionar la memoria conversacional y el contexto.
- Almacenar y consultar el conocimiento de la empresa.
- Aplicar las reglas de negocio.
- Alinear las decisiones con los objetivos de la empresa.
- Ejecutar tareas programadas.
- Auditar todo lo que ocurre en el sistema.
- Proveer seguridad, configuración y utilidades compartidas.
- Exponer interfaces internas para que n8n, los agentes y los conectores interactúen de forma controlada.

## Estructura

```text
core/
├── api/              # Interfaces internas del Core
├── events/           # Event Bus / cola central de eventos
├── scheduler/        # Tareas programadas y recurrentes
├── memory/           # Memoria conversacional y contexto
├── knowledge/        # Conocimiento de la empresa
├── rules/            # Reglas de negocio
├── goals/            # Objetivos de la empresa
├── behavior/         # Comportamiento de CJ_OS
├── policies/         # Políticas de gobierno del sistema
├── reasoning/        # Flujo de razonamiento
├── decision_engine/  # Motor de decisiones
├── audit/            # Auditoría
├── security/         # Autenticación y cifrado
├── config/           # Configuración en runtime
├── utils/            # Utilidades compartidas
└── orchestrator/     # Configuración base para n8n
```

## Los cinco niveles del criterio de CJ_OS

| Nivel | Pregunta que responde | Ejemplo |
|-------|----------------------|---------|
| `memory/` | ¿Qué pasó? | "Francisco pidió 50 tornillos ayer." |
| `knowledge/` | ¿Cómo funciona la empresa? | "El stock mínimo de tornillos es 100." |
| `rules/` | ¿Qué está permitido hacer? | "Solo el encargado de almacén puede autorizar salidas." |
| `goals/` | ¿Qué intenta lograr la empresa? | "Reducir faltantes de inventario en un 20%." |
| `behavior/` | ¿Cómo debe comportarse? | "Preguntar antes de actuar, escribir con claridad, nunca inventar datos." |

## Estado

- Fase M2.1 completada: estructura del Blueprint y del Core actualizada.
- Fase M2.4 en cierre: documentación validada y lista para aprobación de Carlos.
- **Hello World end-to-end en preparación:** se creará el primer script del Core como prueba de comunicación con n8n.
