# CJ_OS (CJ Operating System)

> Nombre interno del proyecto: **CJ_OS**  
> Nombre de carpeta temporal: `CJ_Assistant` (se mantendrá hasta la versión estable v1.0).

## Visión

CJ_OS es el sistema operativo inteligente de la empresa 3P. Orquesta personas, procesos, datos y sistemas externos mediante automatización, eventos e inteligencia artificial.

No es un chatbot. Es un ERP inteligente modular que permite a cada área del negocio contar con un agente de IA especializado, conectado a los sistemas que ya utiliza la empresa.

## Objetivo General

Crear una plataforma centralizada que reciba información desde múltiples canales (WhatsApp, Outlook, etc.), la procese mediante agentes de IA, consulte sistemas internos y externos, y genere acciones, alertas, reportes y respaldos de forma automática.

## Objetivos Específicos

- Centralizar la automatización de procesos de 3P.
- Conectar WhatsApp, Outlook, OneDrive, Google Drive, SAE y Excel de almacén.
- Implementar agentes de IA especializados por área de negocio.
- Mantener archivos como fuente de verdad en `workspace/` y datos estructurados en PostgreSQL.
- Garantizar auditoría, reversibilidad y configuración externa.
- Permitir cambiar de proveedor de IA sin reescribir lógica de negocio.

## Arquitectura General

CJ_OS se ejecuta sobre **Docker Desktop** en Windows 10 Pro. Los servicios principales corren como contenedores dentro de un entorno aislado.

El proyecto reside en: `C:\Projects\CJ_Assistant\`.

### Fuentes de verdad

| Tipo | Fuente de verdad | Contenido |
|------|------------------|-----------|
| Archivos | `workspace/` | PDFs, imágenes, Excel, Word, catálogos |
| Datos estructurados | PostgreSQL | Referencias, índices, estados, relaciones |
| Eventos | `core/audit/events/` | Historial de eventos |
| Configuración | `config/` + `.env` | Variables y archivos de configuración |
| Backups | `runtime/backups/` | Dumps y snapshots |

### Componentes principales

| Componente | Función | Ubicación |
|------------|---------|-----------|
| Docker Desktop | Motor de contenedores | No aplica |
| Event Bus / Queue | Cola central de eventos | `core/events/` |
| Orchestrator (n8n) | Orquestador de flujos. Recibe eventos, los mueve hacia el Core y distribuye respuestas. | `core/orchestrator/` |
| Scheduler | Tareas programadas | `core/scheduler/` |
| PostgreSQL | Datos estructurados | `runtime/database/postgres/` |
| Redis | Caché y colas | `runtime/database/redis/` |
| AI Layer | Proveedores, agentes, prompts, memoria y herramientas | `ai/` |
| Connectors | Conectores con sistemas externos | `connectors/` |
| Modules | Lógica de negocio por área | `modules/` |
| Core | Cerebro del sistema: eventos, scheduler, memoria, auditoría, seguridad, configuración, utilidades y APIs internas | `core/` |
| Documentation | Fuentes oficiales de verdad | `docs/` |

## Principios del Proyecto

- Calidad antes que velocidad.
- Arquitectura antes que código.
- Evidencia antes que suposiciones.
- Documentación antes que memoria.
- Automatizar únicamente cuando el proceso sea estable.
- Cada cambio debe poder revertirse.
- Nunca ocultar errores.
- Informar siempre los riesgos antes de ejecutar una acción.
- Archivos fuera de la base de datos.
- Datos persistentes fuera de Docker.
- Configuración 100% externa.

## Reglas de Desarrollo

- No avanzar al siguiente Milestone sin validación explícita de Carlos.
- No realizar cambios destructivos sin autorización de Carlos.
- Verificar prerrequisitos antes de instalar cualquier componente.
- Validar el sistema después de cada cambio.
- Documentar qué cambió, por qué cambió y cómo revertirlo.
- Mantener la documentación sincronizada con el estado real del proyecto.
- No escribir rutas absolutas ni credenciales en el código.
- Centralizar configuración en `.env` y archivos en `config/`.
- Mantener archivos en `workspace/` y datos estructurados en PostgreSQL.
- Todo evento relevante debe quedar auditado en `core/audit/`.

## Roles del Proyecto

| Rol | Responsable | Responsabilidades |
|-----|-------------|-------------------|
| Product Owner / Director | Carlos | Decisiones de negocio, prioridades y autorizaciones. |
| Ingeniero DevOps | Kimi | Construir, instalar, mantener, probar y documentar el entorno técnico. |
| Arquitecto de Software y Sistemas | ChatGPT | Diseñar arquitectura, definir lógica, revisar calidad, proponer mejoras y validar decisiones técnicas. |

## Metodología

El proyecto se desarrolla por **Milestones** con validación obligatoria entre cada fase:

| Milestone | Nombre | Estado | Propósito |
|-----------|--------|--------|-----------|
| M0 | Preparación del entorno | ✅ Completado | Preparar estructura base y herramientas. |
| M1.0.1 | Revisión de arquitectura técnica | ✅ Completado | Definir arquitectura de carpetas y componentes. |
| M1 | Infraestructura | ✅ Completado | Tener Docker, PostgreSQL, Redis y n8n operativos. |
| M2 | Arquitectura Funcional | ✅ Completado | Definir qué es CJ_OS antes de programar. |
| M2.2 | Arquitectura Cognitiva | ✅ Completado | Definir cómo piensa CJ_OS antes del modelo de datos. |
| M2.3 | Filosofía y Constitución | ✅ Completado | Definir el ADN y comportamiento de CJ_OS. |
| M2.4 | Auditoría y Aprobación Documental | 🔄 En espera de aprobación de Carlos | Validar documentación antes del Modelo de Datos. |
| M2.5 | Ontología Empresarial | ⏳ Pendiente | Definir entidades, atributos y relaciones de 3P. |
| M3 | Modelo de Datos | ⏳ Pendiente | Traducir el diseño funcional a tablas de PostgreSQL. |
| M4 | Integraciones | ⏳ Pendiente | Conectar sistemas externos (WhatsApp, Outlook, SAE, etc.). |
| M5 | Automatización | ⏳ Pendiente | Orquestar flujos con n8n y el Core. |
| M6 | IA | ⏳ Pendiente | Implementar agentes, memoria y abstracción de proveedores. |
| M7 | Producción | ⏳ Pendiente | Seguridad, respaldos, pruebas y lanzamiento. |

## Tecnologías

## Integraciones

## Estructura de Carpetas

```text
CJ_OS/
│
├── .env                              # Variables de entorno globales
├── README.md                         # Resumen ejecutivo
│
├── docs/                             # Documentación oficial
├── config/                           # Configuración por ambiente
│   ├── development/
│   ├── production/
│   └── testing/
│
├── core/                             # Cerebro del sistema
│   ├── api/                          # Interfaces internas del Core
│   ├── events/                       # Event Bus / cola
│   ├── scheduler/                    # Tareas programadas
│   ├── memory/                       # Memoria conversacional y contexto
│   ├── knowledge/                    # Conocimiento de la empresa
│   ├── rules/                        # Reglas de negocio
│   ├── goals/                        # Objetivos de la empresa
│   ├── behavior/                     # Comportamiento de CJ_OS
│   ├── policies/                     # Políticas de gobierno
│   ├── reasoning/                    # Razonamiento paso a paso
│   ├── decision_engine/              # Motor de decisiones
│   ├── audit/                        # Auditoría
│   │   ├── events/
│   │   ├── errors/
│   │   ├── metrics/
│   │   └── snapshots/
│   ├── security/                     # Autenticación y cifrado
│   ├── config/                       # Configuración en runtime
│   ├── utils/                        # Utilidades compartidas
│   └── orchestrator/                 # n8n config y workflows base
│
├── ai/                               # Capa de inteligencia artificial
│   ├── providers/                    # OpenAI, Kimi, Claude, Gemini
│   ├── agents/                       # Agentes especializados
│   ├── prompts/                      # Prompts globales
│   ├── memory/                       # Memoria conversacional
│   └── tools/                        # Herramientas invocables
│
├── connectors/                       # Conectores con sistemas externos
│   ├── whatsapp/
│   ├── google/
│   ├── onedrive/
│   ├── outlook/
│   ├── sae/
│   └── excel/
│
├── modules/                          # Módulos de negocio
│   ├── almacen/
│   ├── ventas/
│   ├── compras/
│   ├── calidad/
│   ├── sgc/
│   ├── rrhh/
│   ├── logistica/
│   └── gerencia/
│
├── workspace/                        # Archivos fuente de verdad
│   ├── almacen/
│   ├── ventas/
│   ├── compras/
│   ├── calidad/
│   ├── sgc/
│   ├── rrhh/
│   ├── logistica/
│   ├── gerencia/
│   └── shared/
│
├── runtime/                          # Datos operativos
│   ├── logs/
│   ├── temp/
│   ├── cache/
│   ├── database/
│   │   ├── postgres/
│   │   └── redis/
│   └── backups/
│
├── prompts/                          # Prompts globales legacy
│
└── testing/                          # Pruebas y validaciones
```

## Core del Sistema

El `core/` es el **cerebro** de CJ_OS. Contiene componentes transversales que no pertenecen a ningún módulo de negocio.

| Componente | Responsabilidad |
|------------|-----------------|
| `core/api/` | Contratos de comunicación interna entre Core, dominios, agentes y n8n. |
| `core/events/` | Event Bus / cola central de eventos. |
| `core/scheduler/` | Programación de tareas recurrentes. |
| `core/memory/` | Memoria conversacional y contexto. Responde "¿qué pasó?". |
| `core/knowledge/` | Conocimiento de la empresa. Responde "¿cómo funciona?". |
| `core/rules/` | Reglas de negocio. Responde "¿qué está permitido?". |
| `core/goals/` | Objetivos de la empresa. Responde "¿qué se intenta lograr?". |
| `core/behavior/` | Comportamiento de CJ_OS. Responde "¿cómo debe comportarse?". |
| `core/policies/` | Políticas transversales de gobierno del sistema. |
| `core/reasoning/` | Flujo de razonamiento paso a paso. |
| `core/decision_engine/` | Motor de decisiones del sistema. |
| `core/audit/` | Registro de eventos, errores, métricas y snapshots. |
| `core/security/` | Autenticación, autorización y cifrado. |
| `core/config/` | Gestión de configuración en runtime. |
| `core/utils/` | Utilidades compartidas por todo el sistema. |
| `core/orchestrator/` | Configuración y workflows base de n8n. |

### Principio arquitectónico

> **n8n = Orquestador**  
> **CJ_OS = Cerebro**

n8n se encarga de mover datos y disparar acciones. El Core se encarga de gobernar, decidir y persistir.

## Módulos de Negocio

Cada módulo encapsula la lógica, reglas, documentación y configuración de un área del negocio.

| Módulo | Responsabilidad |
|--------|-----------------|
| `almacen/` | Inventario, entradas, salidas, stock mínimo. |
| `ventas/` | Cotizaciones, pedidos, clientes. |
| `compras/` | Proveedores, órdenes de compra. |
| `calidad/` | No conformidades, auditorías. |
| `sgc/` | Sistema de Gestión de Calidad (ISO 9001). |
| `rrhh/` | Recursos Humanos, vacaciones, incapacidades. |
| `logistica/` | Envíos, rutas, entregas. |
| `gerencia/` | Dashboards, reportes, indicadores. |

## Agentes de IA

Los agentes viven en `ai/agents/` y se asocian a módulos:

| Agente | Módulo | Especialidad |
|--------|--------|--------------|
| Agente Almacén | `modules/almacen/` | Inventario, stock, entradas, salidas. |
| Agente Calidad | `modules/calidad/` | No conformidades, auditorías, ISO. |
| Agente Ventas | `modules/ventas/` | Cotizaciones, pedidos, clientes. |
| Agente Compras | `modules/compras/` | Proveedores, órdenes de compra. |
| Agente RRHH | `modules/rrhh/` | Vacaciones, incapacidades, personal. |
| Agente Logística | `modules/logistica/` | Envíos, rutas, entregas. |
| Agente Gerencia | `modules/gerencia/` | Reportes, indicadores, decisiones. |

## Abstracción del Proveedor de IA

CJ_OS no depende de una sola IA. La capa `ai/providers/` expone una interfaz común.

```env
IA_PROVIDER=Kimi
IA_PROVIDER_API_KEY=token-seguro
IA_PROVIDER_MODEL=kimi-latest
```

Proveedores soportados:

| Proveedor | Valor de `IA_PROVIDER` |
|-----------|------------------------|
| OpenAI | `OpenAI` |
| Kimi | `Kimi` |
| Anthropic Claude | `Claude` |
| Google Gemini | `Gemini` |

Cambiar de proveedor solo requiere modificar `.env`.

## Flujo General

```text
WhatsApp
    │
    ▼
n8n (Orquestador)
    │
    ▼
CJ_OS Core
    │
    ├─ events/    ← encola y enruta el evento
    ├─ memory/    ← recupera contexto conversacional
    ├─ security/  ← valida permisos y autenticación
    └─ config/    ← carga configuración relevante
    │
    ▼
AI Layer (ai/agents/)
    │
    ▼
Módulo de negocio (modules/<area>/)
    │
    ▼
PostgreSQL
    │
    ▼
Respuesta
    │
    ▼
n8n (Orquestador)
    │
    ▼
WhatsApp / Outlook / Dashboard
```

### Descripción del flujo

1. **WhatsApp** recibe un mensaje del usuario.
2. **n8n** recibe el mensaje mediante webhook y lo envía al Core.
3. **CJ_OS Core** procesa el evento: lo encola, recupera contexto, valida seguridad y carga configuración.
4. **AI Layer** invoca al agente especializado correspondiente.
5. **El agente** consulta el módulo de negocio relevante.
6. **El módulo** lee o escribe en **PostgreSQL** según sea necesario.
7. El Core genera la **respuesta**.
8. **n8n** envía la respuesta al canal correspondiente (WhatsApp, Outlook, etc.).
9. **Audit** registra toda la interacción.

## Roadmap

## Versionado

## Decisiones Técnicas

## Lecciones Aprendidas

## Incidentes

## Checklist de Implementación

## Pendientes

## Ideas Futuras

- Renombrar la carpeta del proyecto de `CJ_Assistant` a `CJ_OS` cuando alcance la versión estable v1.0.
