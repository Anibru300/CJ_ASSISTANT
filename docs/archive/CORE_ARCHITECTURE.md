# Arquitectura del Core de CJ_OS

**Fecha:** 2026-06-25  
**Versión:** 0.0.8  
**Estado:** **OBSOLETO / ARCHIVADO**

> ⚠️ **Este documento quedó archivado durante la auditoría M2.4.** Su contenido fue consolidado en `docs/CJ_OS_BLUEPRINT.md` (Niveles 3, 5, 8, 10 y 12). No debe usarse como fuente de verdad activa. Consúltese el Blueprint para la arquitectura actual del Core.

---

## 1. Principio arquitectónico fundamental

> **n8n = Orquestador**  
> **CJ_OS = Cerebro**

A partir de esta fase, n8n deja de ser considerado el centro del sistema. Su rol se redefine como **orquestador de flujos**: recibe eventos, los mueve entre conectores, dispara llamadas al Core y distribuye respuestas.

El **Core de CJ_OS** asume la responsabilidad de gobernar el sistema: toma de decisiones, gestión de eventos, memoria, auditoría, seguridad, configuración y coordinación con los agentes de IA.

---

## 2. Responsabilidades del Core

El Core es el cerebro transversal de CJ_OS. No contiene lógica de negocio específica de ningún módulo, pero provee las capacidades que todos los módulos, agentes y conectores necesitan.

| Componente | Responsabilidad |
|------------|-----------------|
| `core/api/` | Definir contratos de comunicación interna entre Core, módulos, agentes y n8n. |
| `core/events/` | Recibir, encolar y distribuir eventos. Actúa como Event Bus / cola central. |
| `core/scheduler/` | Ejecutar tareas recurrentes: reportes, respaldos, sincronizaciones, alertas. |
| `core/memory/` | Gestionar memoria conversacional, contexto histórico y estados temporales. |
| `core/audit/` | Registrar eventos, errores, métricas y snapshots para reconstrucción de decisiones. |
| `core/security/` | Autenticación, autorización, cifrado y gestión de secretos. |
| `core/config/` | Cargar y validar configuración desde `.env` y archivos por ambiente. |
| `core/utils/` | Utilidades compartidas: fechas, strings, validaciones, logging, parsing. |
| `core/orchestrator/` | Configuración base y workflows transversales de n8n. |

### Responsabilidades generales del Core

1. **Gobernanza de eventos:** todo evento que entra al sistema pasa por el Core antes de ser procesado por un agente o módulo.
2. **Coordinación con IA:** el Core invoca a los agentes de IA de forma controlada, gestionando contexto y memoria.
3. **Persistencia estructurada:** el Core coordina la lectura y escritura en PostgreSQL, respetando que los archivos vivan en `workspace/`.
4. **Auditoría universal:** toda acción relevante queda registrada.
5. **Seguridad transversal:** autentica y autoriza el acceso a funciones y datos sensibles.
6. **Configuración centralizada:** carga y valida la configuración necesaria para que todos los componentes operen.

---

## 3. Responsabilidades de n8n

n8n es el **orquestador visual y técnico** de CJ_OS. Su trabajo es mover datos y disparar acciones, no tomar decisiones de negocio complejas.

| Responsabilidad | Descripción |
|-------------------|-------------|
| Recepción de eventos externos | Escuchar webhooks desde WhatsApp, Outlook y otros conectores. |
| Enrutamiento inicial | Enviar el evento al Core para su clasificación y priorización. |
| Invocación del Core | Llamar a funciones del Core cuando se requiere procesamiento inteligente. |
| Invocación de conectores | Disparar acciones en sistemas externos: enviar mensaje, crear tarea, sincronizar archivo. |
| Ejecución de workflows transversales | Workflows base definidos en `core/orchestrator/`. |
| Distribución de respuestas | Enviar respuestas de vuelta al canal correspondiente. |

### Lo que n8n NO hace

- No decide qué agente de IA debe responder.
- No contiene lógica de negocio de módulos.
- No almacena datos estructurados de forma permanente.
- No gestiona memoria conversacional.
- No define seguridad ni auditoría.

> n8n es el conductor de la orquesta. El Core es el director.

---

## 4. Responsabilidades de los Connectors

Los conectores viven en `connectors/` y son los puentes entre CJ_OS y los sistemas externos.

| Connector | Responsabilidad |
|-----------|-----------------|
| `connectors/whatsapp/` | Recibir y enviar mensajes, notas de voz, imágenes y documentos por WhatsApp. |
| `connectors/outlook/` | Recibir y enviar correos, consultar calendario, crear tareas. |
| `connectors/onedrive/` | Sincronizar y consultar archivos corporativos en OneDrive. |
| `connectors/google/` | Sincronizar y consultar archivos en Google Drive. |
| `connectors/sae/` | Consultar y, cuando sea posible, actualizar datos del sistema SAE (Aspel). |
| `connectors/excel/` | Leer y actualizar archivos Excel de almacén y otros módulos. |

### Principios de los Connectors

- Cada connector es responsable de **adaptar** el protocolo externo al formato interno de CJ_OS.
- Los connectors no toman decisiones de negocio.
- Los connectors publican eventos en el Core en lugar de invocar directamente a módulos o agentes.
- Toda interacción externa queda auditada.

---

## 5. Responsabilidades de los Módulos

Los módulos viven en `modules/` y encapsulan la lógica, reglas, documentación y configuración de cada área de negocio.

| Módulo | Responsabilidad |
|--------|-----------------|
| `modules/almacen/` | Inventario, entradas, salidas, stock mínimo, consultas de disponibilidad. |
| `modules/ventas/` | Cotizaciones, pedidos, clientes, seguimiento de oportunidades. |
| `modules/compras/` | Proveedores, órdenes de compra, recepciones. |
| `modules/calidad/` | No conformidades, auditorías, acciones correctivas. |
| `modules/sgc/` | Sistema de Gestión de Calidad (ISO 9001), documentación, procesos. |
| `modules/rrhh/` | Recursos Humanos, vacaciones, incapacidades, personal. |
| `modules/logistica/` | Envíos, rutas, entregas, seguimiento. |
| `modules/gerencia/` | Dashboards, reportes, indicadores, decisiones estratégicas. |

### Principios de los Módulos

- Cada módulo es autónomo. Agregar o modificar un módulo no debe afectar a los demás.
- Los módulos exponen su lógica al Core mediante contratos estables.
- Los módulos no acceden directamente a conectores; lo hacen a través del Core.
- Cada módulo tiene su agente de IA especializado en `ai/agents/`.

---

## 6. Flujo principal del sistema

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

---

## 7. Beneficios de esta arquitectura

### Mantenimiento

- El Core centraliza funciones transversales, evitando duplicación de código.
- Cada capa tiene responsabilidades claras y delimitadas.
- Los cambios en un módulo no afectan al resto del sistema.

### Escalabilidad

- El Core permite escalar componentes de forma independiente.
- Los módulos pueden agregarse sin modificar el resto del sistema.
- La abstracción de IA permite cambiar de proveedor sin reescribir lógica.

### Pruebas

- Es posible probar cada capa de forma aislada.
- Los módulos pueden validarse con datos de prueba sin depender de conectores externos.
- El Core puede simular eventos, memoria y respuestas de IA para pruebas automatizadas.

---

## 8. Próximos pasos

1. Completar la Fase M1.3 (levantamiento de n8n).
2. Definir los primeros eventos del Event Bus.
3. Diseñar los contratos internos entre Core y módulos.
4. Comenzar el desarrollo de los primeros conectores (WhatsApp).
