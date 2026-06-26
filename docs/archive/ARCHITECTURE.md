# Arquitectura de CJ_OS v1.0

> ⚠️ **Este documento quedó archivado durante la auditoría M2.4.** Su contenido fue consolidado en `docs/CJ_OS_BLUEPRINT.md` y `docs/SYSTEM_MAP.md`. No debe usarse como fuente de verdad activa.

> **CJ_OS (CJ Operating System)** no es un chatbot.  
> Es un sistema operativo inteligente para la empresa 3P, diseñado para orquestar personas, procesos, datos y sistemas externos mediante automatización, eventos e inteligencia artificial.

---

## 1. Visión

CJ_OS será el centro neurálgico digital de 3P. Recibirá información desde WhatsApp, Outlook y otros canales; la encolará como eventos; la procesará con agentes de IA especializados; ejecutará workflows de automatización; consultará sistemas internos (SAE, Excel de almacén) y sistemas externos (OneDrive, Google Drive); y generará acciones, alertas, reportes y respaldos.

Los **archivos** (PDFs, imágenes, Excel, Word, catálogos) vivirán como fuente de verdad en `workspace/`.  
Los **datos estructurados** (referencias, índices, estados, relaciones) vivirán en PostgreSQL.  
Todo quedará auditado y respaldado.

---

## 2. Principios arquitectónicos

| Principio | Descripción |
|-----------|-------------|
| **Separación de fuentes de verdad** | Archivos en `workspace/`. Datos estructurados en PostgreSQL. Backups en `runtime/backups/`. |
| **Event-driven** | Todo flujo comienza con un evento que entra a una cola. Los componentes están desacoplados. |
| **Modularidad y agentes** | Cada área de negocio tiene su módulo y, dentro de la capa de IA, su agente especializado. |
| **Independencia de IA** | El sistema puede cambiar de proveedor de IA (OpenAI, Kimi, Claude, Gemini) sin reescribir lógica de negocio. |
| **Configuración externa** | Todo se configura mediante `.env` y archivos en `config/`. Nada de rutas absolutas ni credenciales en el código. |
| **Datos fuera de Docker** | Los datos persistentes viven fuera de los contenedores. Docker solo monta volúmenes. |
| **Auditoría obligatoria** | Cada evento, error, métrica y snapshot queda registrado. Toda decisión debe poder reconstruirse. |
| **Reversibilidad** | Cada cambio debe poder revertirse. Todo está documentado. |

---

## 3. Componentes del sistema

### 3.1 Capa de presentación / entrada

| Componente | Función |
|------------|---------|
| **WhatsApp** | Canal principal de comunicación. Recibe mensajes, notas de voz, imágenes y documentos. |
| **Outlook** | Recibe y envía correos, consulta calendario, genera tareas. |
| **Web / Dashboard** | (Futuro) Interfaz visual para monitoreo y administración. |

### 3.2 Core del sistema

El `core/` es el corazón de CJ_OS. No pertenece a ningún módulo de negocio.

| Componente | Función |
|------------|---------|
| **Event Bus** | Cola central de eventos. Recibe, encola y distribuye eventos a los consumidores. Implementado sobre Redis o n8n. |
| **Scheduler** | Programación de tareas recurrentes: reportes diarios, respaldos, sincronizaciones. |
| **Audit** | Registro de eventos, errores, métricas y snapshots. |
| **Security** | Autenticación, autorización, cifrado y gestión de secretos. |
| **Config** | Gestión de configuración en tiempo de ejecución. |
| **Orchestrator (n8n)** | Motor de workflows. Consume eventos del bus y ejecuta flujos. |

### 3.3 Capa de inteligencia artificial

| Componente | Función |
|------------|---------|
| **Providers** | Adaptadores para OpenAI, Kimi, Claude, Gemini u otro proveedor. |
| **Agents** | Agentes especializados por área: Agente Almacén, Agente Calidad, Agente Ventas, etc. |
| **Prompts** | Plantillas de prompts organizadas por agente y módulo. |
| **Memory** | Memoria conversacional y contexto histórico de los agentes. |
| **Tools** | Herramientas que los agentes pueden invocar (consultar stock, crear tarea, enviar mensaje). |

### 3.4 Capa de datos

| Componente | Función |
|------------|---------|
| **PostgreSQL** | Base de datos para referencias, índices, estados y relaciones. **NO almacena archivos.** |
| **Redis** | Caché, sesiones, colas de eventos y estados temporales. |

### 3.5 Capa de conectores

| Componente | Función |
|------------|---------|
| **WhatsApp** | Puente de mensajería. |
| **OneDrive** | Almacenamiento y sincronización de documentos corporativos. |
| **Google Drive** | Integración con archivos compartidos de Google. |
| **Outlook** | Correo y calendario. |
| **SAE (Aspel)** | Consulta de inventario, clientes, facturas y operaciones. |
| **Excel de almacén** | Lectura y actualización de inventario manual. |

### 3.6 Capa de módulos de negocio

Cada módulo encapsula su lógica, reglas, documentación y configuración:

```text
modules/
├── almacen/        # Inventario, entradas, salidas, stock mínimo
├── ventas/         # Cotizaciones, pedidos, clientes
├── compras/        # Proveedores, órdenes de compra
├── calidad/        # No conformidades, auditorías
├── sgc/            # Sistema de Gestión de Calidad (ISO 9001)
├── rrhh/           # Recursos Humanos, vacaciones, incapacidades
├── logistica/      # Envíos, rutas, entregas
└── gerencia/       # Dashboards, reportes, indicadores
```

Cada módulo contiene:

```text
modules/<nombre>/
├── workflows/      # Workflows específicos
├── rules/          # Reglas de negocio
├── prompts/        # Prompts específicos del módulo
├── config/         # Configuración
├── data/           # Datos estructurados del módulo
└── docs/           # Documentación
```

### 3.7 Agentes especializados

Los agentes viven en `ai/agents/` y se asignan a módulos:

| Agente | Módulo asociado | Especialidad |
|--------|-----------------|--------------|
| Agente Almacén | `modules/almacen/` | Inventario, stock, salidas, entradas |
| Agente Calidad | `modules/calidad/` | No conformidades, auditorías, ISO |
| Agente Ventas | `modules/ventas/` | Cotizaciones, pedidos, clientes |
| Agente Compras | `modules/compras/` | Proveedores, órdenes de compra |
| Agente RRHH | `modules/rrhh/` | Vacaciones, incapacidades, personal |
| Agente Logística | `modules/logistica/` | Envíos, rutas, entregas |
| Agente Gerencia | `modules/gerencia/` | Reportes, indicadores, decisiones |

---

## 4. Fuentes de verdad

```text
Workspace          PostgreSQL         Backups
   │                    │                 │
   │ Archivos fuente    │ Datos           │ Copias de
   │ de verdad          │ estructurados   │ seguridad
   │ (PDF, Excel,       │ (referencias,   │ periódicas
   │ imágenes, Word)    │ estados,        │
   │                    │ relaciones)     │
```

| Tipo de dato | Fuente de verdad | Ejemplos |
|--------------|------------------|----------|
| Archivos | `workspace/` | PDFs, imágenes, Excel, Word, catálogos |
| Referencias | PostgreSQL | IDs, estados, relaciones, metadatos |
| Eventos | `core/audit/events/` | Historial de eventos |
| Configuración | `config/` + `.env` | Variables y archivos de configuración |
| Backups | `runtime/backups/` | Dumps de PostgreSQL, snapshots de workspace |

---

## 5. Diagrama arquitectónico

```text
                                  Carlos
                                    │
                       ┌────────────┴────────────┐
                       │                         │
                   WhatsApp                 Web / Dashboard
                       │                         │
                       └────────────┬────────────┘
                                    │
                                    ▼
                          ┌─────────────────┐
                          │  Event Bus /    │
                          │  Queue (Redis)  │
                          └────────┬────────┘
                                   │
          ┌────────────────────────┼────────────────────────┐
          │                        │                        │
          ▼                        ▼                        ▼
   ┌─────────────┐         ┌──────────────┐          ┌─────────────┐
   │  Scheduler  │         │ Orchestrator │          │   Core      │
   │             │         │    (n8n)     │          │ ├─ events   │
   │  Tareas     │         │  Workflows   │          │ ├─ audit    │
   │  recurrentes│         │              │          │ ├─ security │
   └─────────────┘         └──────┬───────┘          │ └─ config   │
                                  │                  └─────────────┘
                                  │
          ┌───────────────────────┼───────────────────────┐
          │                       │                       │
          ▼                       ▼                       ▼
   ┌─────────────┐        ┌──────────────┐        ┌─────────────┐
   │   Agents    │        │  Connectors  │        │  AI Layer   │
   │  Almacén    │        │ ├─ whatsapp  │        │ ├─ providers│
   │  Calidad    │        │ ├─ onedrive  │        │ ├─ prompts  │
   │  Ventas     │        │ ├─ google    │        │ ├─ memory   │
   │  ...        │        │ ├─ outlook   │        │ ├─ agents   │
   └──────┬──────┘        │ ├─ sae       │        │ └─ tools    │
          │               │ └─ excel     │        └─────────────┘
          │               └──────────────┘
          │                       │
          └───────────────────────┘
                          │
                          ▼
              ┌─────────────────────┐
              │     PostgreSQL      │
              │  (datos estructurados)
              └─────────────────────┘
                          │
                          ▼
              ┌─────────────────────┐
              │       Redis         │
              │  (caché y colas)    │
              └─────────────────────┘
                          │
                          ▼
        ┌─────────────────────────────────────┐
        │            Workspace                │
        │  (archivos fuente de verdad)        │
        │  PDFs / Imágenes / Excel / Word     │
        └─────────────────────────────────────┘
                          │
                          ▼
        ┌─────────────────────────────────────┐
        │         Runtime / Backups           │
        │  (logs, temp, cache, dumps)         │
        └─────────────────────────────────────┘
```

---

## 6. Flujo típico de datos

### Ejemplo: Nota de voz de Francisco

```text
1. Francisco envía una nota de voz por WhatsApp.
2. El connector de WhatsApp recibe el mensaje y lo publica en el Event Bus.
3. El Orchestrator (n8n) consume el evento de la cola.
4. n8n descarga el audio y lo envía a un agente de IA.
5. El agente transcribe el audio a texto.
6. El agente interpreta la solicitud y la enruta al Agente Almacén.
7. El Agente Almacén consulta el Excel de almacén y SAE para verificar stock.
8. Si hay stock, genera una salida de material.
9. Si no hay stock, genera una orden de compra.
10. Se actualiza PostgreSQL con referencias y estados.
11. Se guarda evidencia en workspace/.
12. Se registra todo en core/audit/.
13. Se notifica a Ernesto por WhatsApp.
14. Carlos recibe un resumen diario.
```

---

## 7. Abstracción del proveedor de IA

El sistema no depende de una sola IA. La capa `ai/providers/` expone una interfaz común.

Configuración mediante `.env`:

```env
IA_PROVIDER=Kimi
IA_PROVIDER_API_KEY=token-seguro
IA_PROVIDER_MODEL=kimi-latest
IA_PROVIDER_ENDPOINT=https://api.moonshot.cn
```

Posibles valores:

| Proveedor | Valor de `IA_PROVIDER` |
|-----------|------------------------|
| OpenAI | `OpenAI` |
| Kimi | `Kimi` |
| Anthropic Claude | `Claude` |
| Google Gemini | `Gemini` |

Los agentes invocan herramientas y prompts sin saber qué proveedor responde detrás.

---

## 8. Estructura de carpetas definitiva

```text
C:\Projects\CJ_Assistant\
│
├── .env                              # Variables de entorno globales
├── README.md                         # Resumen ejecutivo
│
├── docs/                             # Documentación oficial
│   ├── PROJECT_BIBLE.md
│   ├── ARCHITECTURE.md
│   ├── SYSTEM_MAP.md
│   ├── CHANGELOG.md
│   ├── ROADMAP.md
│   ├── DECISIONS.md
│   ├── TECH_STACK.md
│   ├── ENVIRONMENT.md
│   ├── INSTALL_PLAN.md
│   ├── ROLLBACK_PLAN.md
│   └── INSTALL_LOG.md
│
├── config/                           # Configuración por ambiente
│   ├── development/
│   ├── production/
│   └── testing/
│
├── core/                             # Corazón del sistema
│   ├── scheduler/                    # Tareas programadas
│   ├── events/                       # Event Bus / cola
│   ├── audit/                        # Auditoría
│   │   ├── events/
│   │   ├── errors/
│   │   ├── metrics/
│   │   └── snapshots/
│   ├── security/                     # Autenticación y cifrado
│   ├── config/                       # Configuración en runtime
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
├── prompts/                          # Prompts globales legacy (a migrar a ai/prompts/)
│
└── testing/                          # Pruebas y validaciones
```

---

## 9. Seguridad

| Aspecto | Medida |
|---------|--------|
| Credenciales | En `.env`, nunca en código ni repositorios. |
| Acceso a n8n | Autenticación básica + clave de encriptación. |
| Base de datos | Contraseñas fuertes, acceso solo desde red interna de Docker. |
| API Keys | Rotación periódica y almacenamiento seguro. |
| Auditoría | Todo evento y error queda registrado en `core/audit/`. |
| Respaldos | Dumps automáticos de PostgreSQL y snapshots de workspace en `runtime/backups/`. |

---

## 10. Escalabilidad

A corto plazo todo correrá en una sola máquina Windows con Docker Desktop. A mediano plazo, si el volumen de trabajo lo requiere, se podrá migrar a:

- Servidor dedicado con Docker en Linux.
- Kubernetes para orquestación.
- Servicios gestionados en la nube (RDS para PostgreSQL, ElastiCache para Redis).
- RabbitMQ o Kafka para el Event Bus si el volumen de eventos crece.

La arquitectura de agentes, módulos, conectores y abstracción de IA facilita esta migración.

---

## 11. Estado del diseño

| Elemento | Estado |
|----------|--------|
| Visión de CJ_OS | ✅ Definida |
| Fuentes de verdad separadas | ✅ Definidas |
| Event Bus / Queue | ✅ Definido |
| Core del sistema | ✅ Definido |
| Capa de IA con agentes | ✅ Definida |
| Connectores | ✅ Definidos |
| Módulos de negocio | ✅ Definidos |
| Auditoría | ✅ Definida |
| Configuración por ambiente | ✅ Definida |
| Estructura de carpetas | ✅ Definida |
| Seguridad | ✅ Definida |
| Escalabilidad | ✅ Definida |

---

## 12. Próximos pasos

Una vez aprobada esta arquitectura:

1. Reorganizar físicamente las carpetas del proyecto según la estructura definitiva.
2. Crear el archivo `.env` con la configuración inicial.
3. Crear archivos de configuración en `config/development/`.
4. Crear el `docker-compose.yml` con n8n, PostgreSQL y Redis.
5. Instalar Docker Desktop.
6. Levantar los servicios base.
7. Comenzar a implementar el primer agente/módulo (recomendado: `almacen`).
