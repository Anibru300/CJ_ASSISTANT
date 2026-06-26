# CJ_OS Blueprint v1.0

**Versión:** 0.7.0  
**Fecha:** 2026-06-25  
**Estado:** Pendiente de aprobación por Carlos (M2.8 BKA / KES en preparación)  
**Propietario:** Carlos (Product Owner)  
**Colaboradores:** Kimi (DevOps), ChatGPT (Arquitecto)

---

## Fuentes de verdad documentales

A partir de la auditoría M2.4, la documentación de CJ_OS se consolidó en las siguientes fuentes de verdad:

| Documento | Propósito | Tipo |
|-----------|-----------|------|
| `docs/CJ_OS_FRAMEWORK.md` | Metodología reutilizable de implementación. | Maestro |
| `docs/CJ_OS_BLUEPRINT.md` | Arquitectura maestra del sistema. | Maestro |
| `docs/CJ_OS_PHILOSOPHY.md` | Comportamiento, valores y Constitución de CJ_OS. | Maestro |
| `docs/CJ_OS_OPERATING_MODEL.md` | Modelo operativo de la empresa 3P. | Maestro |
| `docs/CJ_OS_ONTOLOGY.md` | Ontología empresarial: entidades, atributos, restricciones. | Maestro |
| `docs/CJ_OS_KNOWLEDGE_GRAPH.md` | Grafo de conocimiento: relaciones entre entidades. | Maestro |
| `docs/CJ_OS_DECISION_CATALOG.md` | Catálogo de decisiones empresariales. | Maestro |
| `docs/CJ_OS_RULES_CATALOG.md` | Catálogo de reglas de negocio. | Maestro |
| `docs/CJ_OS_EVENT_CATALOG.md` | Catálogo de eventos de negocio. | Maestro |
| `docs/ROADMAP.md` | Planificación por milestones. | Planificación |
| `docs/DECISIONS.md` | Historial de decisiones arquitectónicas. | Historial |
| `docs/SYSTEM_MAP.md` | Mapa visual de referencia rápida. | Soporte visual |

> **Nota:** `docs/CORE_ARCHITECTURE.md` y `docs/ARCHITECTURE.md` fueron archivados y consolidados en este Blueprint. Su contenido quedó absorbido por los Niveles 3, 5, 8 y 11 de este documento.

---

# Nivel 0 — Visión

> **CJ_OS no es un chatbot.**  
> **CJ_OS no es un workflow.**  
> **CJ_OS es un Sistema Operativo Empresarial.**

## Misión

Centralizar toda la operación de la empresa, automatizar procesos y asistir en la toma de decisiones utilizando inteligencia artificial.

CJ_OS será el cerebro digital de 3P. Conectará personas, procesos, datos y sistemas externos en una sola plataforma coherente.

> **CJ_OS es una plataforma reutilizable.** Su motor (eventos, decisiones, memoria, agentes, seguridad, auditoría) es genérico. Lo que hace único a CJ_OS en cada empresa es el **Knowledge Pack**: el paquete de conocimiento empresarial documentado en el Operating Model, Business Dictionary, Ontología, Catálogos, Cognitive Model y Knowledge Graph.
>
> ```text
> CJ_OS Engine + Knowledge Pack 3P = 3P funcionando
> CJ_OS Engine + Knowledge Pack Empresa B = Empresa B funcionando
> CJ_OS Engine + Knowledge Pack Empresa C = Empresa C funcionando
> ```
>
> El motor nunca cambia. Solo cambian los Knowledge Packs.

## ¿Qué hace diferente a CJ_OS?

| Asistente tradicional | CJ_OS |
|-----------------------|-------|
| Responde preguntas. | Toma decisiones y ejecuta acciones. |
| Recuerda conversaciones. | Tiene memoria, conocimiento, reglas y objetivos. |
| Depende de una sola IA. | Usa un motor de IA multi-modelo. |
| Funciona en silos. | Integra WhatsApp, Outlook, SAE, Excel, Drive y más. |
| Olvida el contexto. | Aprende de la operación diaria. |

---

# Nivel 1 — Principios

Estos principios influirán en todas las decisiones futuras del sistema.

| Principio | Descripción |
|-----------|-------------|
| **Una sola fuente de verdad** | Cada dato tiene un único lugar de referencia oficial. Archivos de negocio en `workspace/`. Datos estructurados en PostgreSQL. Evidencia no estructurada en el Data Lake. |
| **Modularidad** | Cada dominio puede crecer sin afectar a los demás. |
| **IA intercambiable** | Ningún proveedor de IA es indispensable. El Motor de IA selecciona el mejor modelo para cada tarea. |
| **Todo debe ser auditable** | Toda decisión, evento, error y acción queda registrada. |
| **Automatización antes que trabajo manual** | Si un proceso se puede automatizar de forma segura, CJ_OS lo automatiza. |
| **Los datos pertenecen a CJ_OS, no a un proveedor** | Los proveedores de IA, mensajería o almacenamiento son reemplazables. |
| **Ningún proveedor externo debe ser indispensable** | Si WhatsApp, OpenAI, Kimi u otro servicio falla, CJ_OS debe poder continuar o alertar con un plan B. |
| **Seguridad por diseño** | Usuarios, permisos, cifrado y auditoría desde el primer día. |
| **Dominio antes de código** | No se programa nada hasta que el negocio esté definido. |
| **Decisiones antes de respuestas** | CJ_OS no solo responde; decide qué acción tomar según reglas y objetivos. |

---

# Nivel 2 — Dominios funcionales de la empresa

En lugar de preguntar "¿qué módulos tendrá CJ_OS?", preguntamos:

> **¿Qué sabe hacer una empresa?**

CJ_OS debe representar una empresa completa. Para 3P, los dominios de negocio reales son:

## Dominios operativos de 3P

| ID | Dominio | ¿Qué responde? | Procesos clave |
|----|---------|----------------|----------------|
| D1 | **Dirección** | ¿Hacia dónde va la empresa? | Objetivos, KPIs, reportes ejecutivos, decisiones estratégicas, gobierno del SGC. |
| D2 | **Ventas** | ¿Cómo entra el dinero? | Clientes, cotizaciones, pedidos, descuentos, facturación inicial, postventa. |
| D3 | **Compras** | ¿Qué se compra y a quién? | Proveedores, cotizaciones de compra, órdenes de compra, recepciones, evaluación de proveedores. |
| D4 | **Almacén** | ¿Dónde está la mercancía? | Entradas, salidas, inventarios, ajustes, mermas, transferencias, máximos/mínimos, material indirecto, devoluciones, evidencias fotográficas, auditorías 5S. |
| D5 | **Logística** | ¿Cómo llega al cliente? | Planeación de rutas, empaque, guías, transportistas, seguimiento de entregas, devoluciones. |
| D6 | **Calidad** | ¿Cumple con el estándar? | Inspecciones, no conformidades, acciones correctivas, control de proveedores, auditorías, 5S, documentación ISO. |
| D7 | **Contabilidad** | ¿Cuánto se debe y cuánto se tiene? | Facturación, cuentas por cobrar/pagar, nómina, pagos, estados financieros, cumplimiento fiscal. |
| D8 | **RRHH** | ¿Quién trabaja en la empresa? | Empleados, asistencia, permisos, vacaciones, capacitación, documentación interna. |
| D9 | **Inteligencia Empresarial** | ¿Qué nos dicen los datos? | Indicadores, reportes, alertas, análisis de tendencias, auditorías de datos, dashboards. |

## Dominios habilitadores de CJ_OS

| ID | Dominio | ¿Qué responde? |
|----|---------|----------------|
| D10 | **Automatización / Tecnología** | ¿Cómo orquesta CJ_OS los flujos? Workflows, conectores, n8n, reglas del Core, agentes de IA. |
| D11 | **Infraestructura / Seguridad** | ¿Sobre qué corre el sistema? Docker, PostgreSQL, Redis, backups, credenciales, accesos, logs. |

> **Nota:** Los dominios operativos (D1-D9) son los que se adquirirán en las **Knowledge Engineering Sessions (M2.8 BKA/KES)**. Los dominios habilitadores (D10-D11) son responsabilidad del equipo técnico y se documentan en el Blueprint y en `docs/SYSTEM_MAP.md`.

---

# Nivel 3 — Arquitectura general

## 3.1 Principio arquitectónico

> **n8n = Orquestador**  
> **CJ_OS = Cerebro**

n8n mueve datos y dispara acciones. CJ_OS decide, recuerda, conoce, aplica reglas y persigue objetivos.

## 3.2 Flujo principal

```text
WhatsApp / Outlook / Drive / SAE / Excel / Scheduler
    │
    ▼
n8n (Orquestador)
    │
    ▼
CJ_OS Core
    │
    ├─ events/           ← recibe y encola eventos
    ├─ memory/           ← recupera contexto
    ├─ knowledge/        ← consulta cómo funciona la empresa
    ├─ rules/            ← aplica reglas de negocio
    ├─ goals/            ← alinea con objetivos
    ├─ behavior/         ← aplica comportamiento de CJ_OS
    ├─ policies/         ← aplica políticas del sistema
    ├─ reasoning/        ← estructura el razonamiento
    ├─ decision_engine/  ← decide qué acción tomar
    ├─ audit/            ← registra toda acción
    └─ security/         ← valida permisos
    │
    ▼
Motor de IA
    │
    ├─ Selecciona modelo según tarea
    ├─ Invoca al proveedor adecuado
    └─ Recibe respuesta estructurada
    │
    ▼
Consejo de Agentes
    │
    ├─ Arquitecto
    ├─ Operaciones
    ├─ Calidad
    ├─ Compras
    ├─ Ventas
    ├─ Inventario
    ├─ Automatización
    ├─ RRHH
    └─ ...
    │
    ▼
Dominio funcional (Ventas, Almacén, Calidad, etc.)
    │
    ▼
Connector (SAE, Excel, Outlook, Drive)
    │
    ▼
PostgreSQL + workspace/
    │
    ▼
Acción / Respuesta
    │
    ▼
n8n (Orquestador)
    │
    ▼
WhatsApp / Outlook / Dashboard
```

---

# Nivel 4 — Motor de IA multi-modelo

## 4.1 Propósito

CJ_OS no dependerá de una sola IA. El Motor de IA seleccionará el mejor modelo para cada tarea.

## 4.2 Asignación inicial de modelos

| Tarea | IA recomendada | Razón |
|-------|----------------|-------|
| Programación | Kimi Code | Optimizado para código y arquitectura técnica. |
| Arquitectura | ChatGPT | Fuerte en diseño de sistemas y razonamiento estructural. |
| Redacción | ChatGPT | Alta calidad de texto en español. |
| Investigación | Gemini | Buen acceso a información actual y búsqueda. |
| Documentos largos | Claude | Gran ventana de contexto. |
| Análisis rápido | Qwen | Eficiente y económico. |
| Local / offline | Ollama | Funciona sin conexión a internet. |

## 4.3 Estrategia de selección

El Motor de IA decidirá según:

1. Tipo de tarea.
2. Longitud del contexto.
3. Costo disponible.
4. Disponibilidad del proveedor.
5. Calidad requerida.
6. Necesidad de privacidad (local vs. nube).

## 4.4 Intercambiabilidad

Si mañana aparece un proveedor mejor, solo se actualiza el Motor de IA. El resto de CJ_OS sigue funcionando igual.

---

# Nivel 5 — Memoria, conocimiento, reglas, objetivos y comportamiento

CJ_OS no solo tendrá memoria. Tendrá **criterio**.

## 5.1 Los cinco niveles

| Nivel | Pregunta que responde | Ejemplo |
|-------|----------------------|---------|
| **Memoria** | ¿Qué pasó? | "Francisco pidió 50 tornillos ayer." |
| **Conocimiento** | ¿Cómo funciona la empresa? | "El stock mínimo de tornillos es 100." |
| **Reglas** | ¿Qué está permitido hacer? | "Solo el encargado de almacén puede autorizar salidas." |
| **Objetivos** | ¿Qué intenta lograr la empresa? | "Reducir faltantes de inventario en un 20%." |
| **Behavior** | ¿Cómo debe comportarse? | "Preguntar antes de actuar, escribir con claridad, nunca inventar datos." |

## 5.2 Por qué esto es diferente

Un chatbot que solo "recuerda" conversaciones puede responder preguntas. CJ_OS, al combinar memoria, conocimiento, reglas, objetivos y comportamiento, puede tomar decisiones consistentes con la cultura y operación real de la empresa.

## 5.3 Aplicación

- **Memoria:** conversaciones, eventos, decisiones previas.
- **Conocimiento:** procedimientos ISO, catálogos, manuales, configuración.
- **Reglas:** permisos, límites, validaciones, políticas.
- **Objetivos:** metas de negocio, KPIs, planes de mejora.
- **Behavior:** tono, estilo, valores, niveles de autonomía, modelo de aprendizaje.

---

# Nivel 6 — Flujos principales

## 6.1 Ejemplo: Pedido por WhatsApp

```text
1. Cliente envía mensaje por WhatsApp pidiendo cotización.
2. n8n recibe el mensaje y lo envía al Core.
3. Core recupera memoria del cliente y contexto de conversación.
4. Motor de IA selecciona el modelo adecuado.
5. Agente de Ventas consulta catálogo y precios.
6. Core valida reglas comerciales.
7. Se genera cotización y se guarda en PostgreSQL.
8. Se envía cotización por WhatsApp.
9. Auditoría registra toda la interacción.
```

## 6.2 Ejemplo: Alerta de inventario bajo

```text
1. Scheduler dispara revisión de inventario.
2. Core consulta SAE y Excel de almacén.
3. Motor de IA analiza tendencias.
4. Core detecta que un producto está por debajo del stock mínimo.
5. Se genera orden de compra sugerida.
6. Se notifica a Compras por Outlook/WhatsApp.
7. Se registra evento en auditoría.
```

## 6.3 Ejemplo: Auditoría de calidad

```text
1. Ernesto reporta una no conformidad por WhatsApp.
2. Core enruta al dominio de Calidad.
3. Agente de Calidad consulta procedimientos ISO.
4. Core aplica reglas de acciones correctivas.
5. Se genera registro en PostgreSQL.
6. Se asigna tarea de seguimiento.
7. Se notifica a responsables.
```

---

# Nivel 7 — Capacidades esperadas

## 7.1 A 6 meses

- [ ] Leer correos de Outlook y clasificarlos.
- [ ] Responder mensajes de WhatsApp de forma contextual.
- [ ] Consultar y actualizar información en SAE.
- [ ] Leer y actualizar archivos Excel.
- [ ] Generar reportes diarios, semanales y mensuales.
- [ ] Crear y actualizar procedimientos ISO.
- [ ] Auditar procesos de almacén y calidad.
- [ ] Generar órdenes de compra sugeridas.
- [ ] Analizar tendencias de inventario.
- [ ] Crear dashboards de indicadores.
- [ ] Controlar proyectos y tareas pendientes.
- [ ] Permitir interacción por voz.
- [ ] Recordar contexto entre conversaciones.
- [ ] Aprender de correcciones y aprobaciones de usuarios.

## 7.2 A 2 años

- [ ] Predicción de demanda de inventario.
- [ ] Automatización completa de cotizaciones.
- [ ] Gestión integral de calidad ISO y NOM-035.
- [ ] Dashboards predictivos para dirección.
- [ ] Integración con proveedores y clientes.
- [ ] Control financiero básico.
- [ ] Gestión de proyectos y recursos.
- [ ] Asistente de voz multicanal.
- [ ] Capacidad de reentrenamiento continuo con datos de 3P.

---

# Nivel 8 — Arquitectura Cognitiva

CJ_OS no es solo memoria e IA. Debe tener una forma de pensar.

## 8.1 El Motor de Decisiones

El `core/decision_engine/` es el corazón de CJ_OS. No es un LLM. Es el cerebro que decide qué hacer ante cada evento.

### Ejemplo: Francisco manda una foto

El Motor de Decisiones no responde "la guardo". Se pregunta:

```text
¿Qué recibí?
    ↓
¿A quién pertenece?
    ↓
¿Es una evidencia?
    ↓
¿Es un catálogo?
    ↓
¿Es una factura?
    ↓
¿Es una foto de almacén?
    ↓
¿Debe ir a Google Drive?
    ↓
¿Debe ir a OneDrive?
    ↓
¿Debe crear una tarea?
    ↓
¿Debe avisarle a Carlos?
    ↓
¿Debe ignorarla?
```

### Responsabilidades del Motor de Decisiones

- Clasificar eventos entrantes.
- Evaluar contexto, conocimiento, reglas, objetivos, políticas y comportamiento.
- Decidir si actúa, pide confirmación o escala.
- Seleccionar el agente o especialista adecuado.
- Registrar la cadena de decisión en auditoría.

## 8.2 El flujo de razonamiento

El `core/reasoning/` define cómo piensa CJ_OS paso a paso.

```text
Observación
    ↓
Clasificación
    ↓
Contexto
    ↓
Reglas
    ↓
Objetivos
    ↓
Políticas
    ↓
Evaluación
    ↓
Acción
    ↓
Auditoría
```

Cada paso produce un resultado que alimenta el siguiente. El razonamiento debe poder reconstruirse para auditoría.

## 8.3 El sistema de políticas

El `core/policies/` define reglas transversales que no son de negocio, sino de gobierno del sistema.

| Política | Descripción |
|----------|-------------|
| **Seguridad** | Quién puede ver o modificar qué. |
| **Prioridad** | Qué eventos se atienden primero. |
| **Privacidad** | Qué datos no pueden salir de la empresa. |
| **Automatización** | Qué acciones pueden ejecutarse solas y cuáles requieren confirmación. |
| **Costos** | Límites de uso de APIs de IA y servicios externos. |
| **Escalamiento** | Cuándo y cómo avisar a un humano. |
| **IA** | Qué tareas pueden resolverse con IA y cuáles no. |
| **Backups** | Qué datos se respaldan, con qué frecuencia y dónde. |

## 8.4 Datos, conocimiento e inteligencia

CJ_OS separa tres conceptos fundamentales:

| Concepto | Definición | Ejemplo |
|----------|------------|---------|
| **Datos** | Hechos concretos de la operación. | Factura 231, cliente X, producto Y, precio Z. |
| **Conocimiento** | Cómo funciona la empresa y sus procesos. | Así funciona SAE. Así funciona ISO 9001. Así se hace un inventario. |
| **Inteligencia** | Capacidad de decidir qué hacer con los datos y el conocimiento. | Con esa información, ¿qué hago? |

Esta separación permite que CJ_OS evolucione sin confundir hechos, procesos y decisiones.

### 8.4.1 Tres niveles de almacenamiento de la información

| Nivel | Tipo de información | Dónde vive | Ejemplos |
|-------|---------------------|------------|----------|
| **Nivel 1 — Conocimiento estratégico** | Reglas, políticas, ontología, decisiones, modelo cognitivo. | **Core** de CJ_OS (memoria semántica y motor de decisiones). | "Nunca existencia negativa", "No modificar vale cerrado". |
| **Nivel 2 — Conocimiento operativo** | Datos transaccionales del negocio. | **PostgreSQL** (base de datos estructurada). | Inventario, pedidos, compras, movimientos. |
| **Nivel 3 — Evidencia** | Documentos, archivos, comunicaciones, fotos, audios. | **Data Lake** (almacenamiento de archivos/binarios). | PDFs, fotos, Excel, correos, WhatsApp, manuales. |

> Esta separación permite escalar: el Core no se llena de archivos, la base de datos no almacena blobs pesados y el Data Lake conserva evidencia sin estructurar.

## 8.5 El Consejo de Agentes

CJ_OS no tendrá un único agente. Tendrá un **Consejo de Agentes Especializados**.

```text
                 CJ_OS
                   │
      ┌────────────┼────────────┐
 Arquitecto    Operaciones     Calidad
      │              │              │
 Compras       Inventario      ISO
      │              │              │
 Ventas       Automatización   RRHH
```

### Principios del Consejo

- Cada agente es experto en un dominio.
- Una solicitud se enruta al agente más adecuado.
- Si un evento afecta múltiples dominios, los agentes colaboran.
- El Motor de Decisiones coordina al Consejo.
- Ningún agente toma decisiones fuera de su especialidad.

### Agentes propuestos

| Agente | Especialidad |
|--------|--------------|
| Arquitecto | Diseño de sistemas, estructura, integraciones. |
| Operaciones | SAE, inventario, compras, almacén, logística. |
| Calidad | ISO 9001, NOM-035, auditorías, acciones correctivas. |
| Compras | Proveedores, órdenes de compra, cotizaciones. |
| Ventas | Clientes, cotizaciones, pedidos, CRM. |
| Inventario | Stock, entradas, salidas, stock mínimo. |
| Automatización | Workflows, triggers, scheduler. |
| RRHH | Personal, vacaciones, incapacidades. |
| Dirección | Indicadores, reportes, decisiones estratégicas. |

## 8.6 Criterios para decidir cuándo actuar, pedir confirmación o escalar

| Situación | Comportamiento de CJ_OS |
|-----------|-------------------------|
| Acción segura y autorizada | Ejecuta automáticamente. |
| Acción con riesgo moderado | Pide confirmación al usuario. |
| Acción no autorizada | Bloquea y registra en auditoría. |
| Incertidumbre alta | Escala a un humano. |
| Error o falla externa | Intenta alternativa o alerta a soporte. |
| Costo alto de IA | Selecciona modelo más económico o pide aprobación. |

---

# Nivel 9 — Cambios recientes y consolidación (M2.4)

## Modificaciones aplicadas en esta versión

1. **Niveles de Inteligencia unificados a 5 capas:**
   - Memory → Knowledge → Rules → Goals → Behavior.
   - `Behavior` ahora es capa de ejecución explícita, no dependencia implícita.

2. **Flujo principal de decisión actualizado:**
   - Incluye lectura de `core/behavior` como paso explícito.
   - El motor de decisiones evalúa conocimiento, reglas, objetivos, políticas y comportamiento.

3. **Core Architecture integrado:**
   - Los 15 componentes del Core están reflejados en Niveles 3, 5, 8 y 11.
   - Los documentos `docs/CORE_ARCHITECTURE.md` y `docs/ARCHITECTURE.md` quedan archivados.

4. **Filosofía y Constitución citadas explícitamente:**
   - Nivel 11 referencia a `CJ_OS_PHILOSOPHY.md` como fuente maestra.
   - Las 8 leyes y niveles de autonomía se mencionan como restricciones de diseño.

5. **Modelo Operativo de la Empresa como requisito previo a M3:**
   - Se agregó el milestone M2.5 y el documento `docs/CJ_OS_OPERATING_MODEL.md`.
   - El Modelo de Datos (M3) no inicia hasta aprobación del Blueprint + Modelo Operativo.

6. **Business Knowledge Acquisition (M2.8) antes de M3:**
   - Se agregó el milestone M2.8 para adquirir conocimiento experto dominio por dominio.
   - M3 queda bloqueado hasta aprobación de M2.8.

7. **Dominios funcionales ajustados a 3P:**
   - Nivel 2 del Blueprint ahora define 9 dominios operativos: Dirección, Ventas, Compras, Almacén, Logística, Calidad, Contabilidad, RRHH e Inteligencia Empresarial.
   - Se separaron Compras, Logística y Contabilidad de dominios genéricos para reflejar la operación real.

8. **Fichas maestras por dominio en el Modelo Operativo:**
   - Cada dominio se documenta con la misma estructura: Objetivo, AS-IS, TO-BE, Automatización futura, Actores, Objetos, Eventos, Procesos, Reglas, Lo que CJ_OS debe saber, Excepciones, Decisiones, KPIs, Matriz de madurez y Pregunta final.
   - Almacén queda como ficha patrón para las siguientes sesiones de M2.8 BKA/KES.

9. **Enfoque event-driven confirmado:**
   - Todo en CJ_OS vive por eventos: `llego_mercancia`, `se_creo_vale`, `se_detecto_merma`, etc.
   - Esto alimenta el Event Bus, los agentes, los logs y las automatizaciones de n8n.

10. **M2.8 es Business Knowledge Acquisition (BKA):**
    - El objetivo de M2.8 es **adquirir el conocimiento empresarial** que CJ_OS necesita para operar.
    - Cada dominio se documenta en tres versiones: AS-IS, TO-BE y Automatización futura.

11. **Meta estratégica del proyecto:**
    - **Separar el motor de CJ_OS del conocimiento específico de cada empresa.**
    - El Core será genérico y reutilizable; lo que cambiará entre empresas será el conocimiento del negocio.
    - Esto convierte a CJ_OS de asistente en **plataforma reutilizable**.

12. **Metodología CJ_OS Framework documentada:**
    - `docs/CJ_OS_FRAMEWORK.md` define la metodología reutilizable.
    - Blueprint → Ontología → Operating Model → Knowledge Graph → Decision Catalog → Rules Catalog → Event Catalog → Data Model → Automation → AI.
    - Cada capa es un documento maestro. El motor permanece intacto cuando cambia el negocio.

13. **Knowledge Engineering Sessions (KES/SIC):**
    - Las sesiones de adquisición dejan de llamarse "Sesiones" para llamarse **Knowledge Engineering Sessions** / Sesiones de Ingeniería del Conocimiento.
    - No son entrevistas: son extracción estructurada de conocimiento experto.

## Relación con otros documentos

```text
CJ_OS_BLUEPRINT     → Arquitectura técnica y funcional
       ↑
CJ_OS_PHILOSOPHY    → Comportamiento, Constitución, valores
       ↑
CJ_OS_OPERATING_MODEL → Procesos, roles, flujos de negocio
       ↑
DECISIONS           → Historial de decisiones arquitectónicas
       ↑
ROADMAP             → Planificación de milestones
       ↑
SYSTEM_MAP          → Representación visual resumida
```

---

# Nivel 10 — Criterios de aprobación del Blueprint

El Blueprint se considerará aprobado cuando:

- [ ] La visión y principios estén claros y alineados con Carlos.
- [ ] Todos los dominios funcionales estén definidos.
- [ ] Los usuarios, roles y permisos estén completos.
- [ ] El Motor de IA multi-modelo esté diseñado.
- [ ] Los cinco niveles (memoria, conocimiento, reglas, objetivos, behavior) estén definidos.
- [ ] La Arquitectura Cognitiva esté documentada (motor de decisiones, razonamiento, políticas, Consejo de Agentes).
- [ ] La separación entre datos, conocimiento e inteligencia esté clara.
- [ ] La Filosofía y Constitución de CJ_OS estén aprobadas (`docs/CJ_OS_PHILOSOPHY.md`).
- [ ] La quinta capa (Behavior) esté definida.
- [ ] El Modelo Operativo de la Empresa esté aprobado (`docs/CJ_OS_OPERATING_MODEL.md`).
- [ ] El Business Knowledge Acquisition (M2.8) esté completado y todos los dominios operativos adquiridos y validados.
- [ ] Los flujos principales estén documentados.
- [ ] Las capacidades a 6 meses y 2 años estén aprobadas.
- [ ] ChatGPT (Arquitecto) haya revisado y validado el diseño.
- [ ] Kimi (DevOps) haya confirmado que la arquitectura técnica puede soportarlo.

---

# Nivel 11 — Filosofía y Constitución

CJ_OS no es solo tecnología. Es un empleado digital. Por eso tiene una filosofía propia.

## 11.1 Misión

> Ser el empleado digital más confiable de 3P.

## 11.2 Valores

- Confianza, responsabilidad, servicio, precisión, mejora continua, seguridad, trazabilidad, humildad operativa.

## 11.3 Comportamiento

- Escribe con claridad, tono profesional y amigable.
- Toma decisiones conservadoras en acciones irreversibles.
- Pide confirmación ante incertidumbre o riesgo.
- Nunca inventa datos.
- Prioriza: personas, datos, clientes, operación, velocidad.
- Aprende proponiendo cambios, no aplicándolos solo.

## 11.4 Constitución de CJ_OS

1. Nunca perder información.
2. Nunca modificar datos críticos sin autorización.
3. Toda acción importante debe poder auditarse.
4. La automatización nunca debe reducir la trazabilidad.
5. Cuando exista incertidumbre alta, preguntar antes de actuar.
6. La empresa siempre tiene prioridad sobre la comodidad del sistema.
7. Los humanos siempre pueden anular una decisión.
8. Toda decisión debe poder explicarse.

## 11.5 Niveles de autonomía

CJ_OS opera con seis niveles de autonomía, detallados en `docs/CJ_OS_OPERATING_MODEL.md`:

| Nivel | Nombre | Comportamiento |
|-------|--------|----------------|
| A0 | Solo informar | Muestra datos y alertas. No decide. |
| A1 | Recomendar | Sugiere y espera aprobación. |
| A2 | Ejecutar tareas reversibles | Actúa solo en acciones de bajo impacto. |
| A3 | Ejecutar procesos autorizados | Ejecuta procesos previamente aprobados. |
| A4 | Requiere aprobación humana | Pregunta antes de ejecutar. |
| A5 | Nunca permitido | Solo informa o escala. |

## 11.6 Documento maestro

La fuente de verdad completa está en `docs/CJ_OS_PHILOSOPHY.md`.

---

# Nivel 12 — Notas de construcción

## 12.1 Qué NO se hará hasta aprobación del Blueprint + Ontología + Knowledge Graph + Catálogos + Modelo Operativo + BKA

- No se crearán tablas de PostgreSQL.
- No se programará código.
- No se crearán APIs.
- No se crearán módulos.
- No se conectarán integraciones externas.

## 12.2 Qué sigue después del Blueprint + Modelo Operativo

Una vez aprobados el Blueprint, la Ontología, el Knowledge Graph, los Catálogos de Eventos/Decisiones/Reglas, el Modelo Operativo y el Business Knowledge Acquisition (M2.8), el siguiente paso será el **Milestone M3 — Modelo de Datos**, donde las tablas, entidades y relaciones surgirán directamente del conocimiento empresarial adquirido.

---

# Control de versiones

| Versión | Fecha | Cambio |
|---------|-------|--------|
| 0.0.1 | 2026-06-25 | Estructura inicial del Blueprint. |
| 0.1.0 | 2026-06-25 | Reestructuración completa: visión, principios, dominios, motor de IA, memoria/conocimiento/reglas/objetivos, flujos y criterios de aprobación. |
| 0.2.0 | 2026-06-25 | Consolidación documental M2.4: unificación de 5 capas cognitivas, integración de CORE_ARCHITECTURE, inclusión de Modelo Operativo como requisito previo a M3. |
| 0.3.0 | 2026-06-25 | Ajuste de dominios funcionales a 9 dominios operativos de 3P, inclusión de Business Design Review (M2.6) y refinamiento del Modelo Operativo. |
| 0.4.0 | 2026-06-25 | Adopción de fichas maestras por dominio en el Modelo Operativo, ficha patrón de Almacén y enfoque event-driven como núcleo del diseño. |
| 0.5.0 | 2026-06-25 | Renombrado M2.x a Business Knowledge Acquisition (BKA), tres versiones por dominio (AS-IS/TO-BE/Automatización), secciones de conocimiento y excepciones, matriz de madurez y meta de separación motor/conocimiento. |
| 0.6.0 | 2026-06-25 | Reorganización metodológica completa: M2.1-M2.8, Ontología, Knowledge Graph, Catálogos de Eventos/Decisiones/Reglas, Knowledge Engineering Sessions (KES/SIC) y framework reutilizable. |
| 0.7.0 | 2026-06-25 | Agregado concepto de Knowledge Pack, arquitectura de tres niveles de información (Core / PostgreSQL / Data Lake) y fuente de verdad extendida. |
