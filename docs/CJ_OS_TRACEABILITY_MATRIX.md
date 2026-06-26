# Traceability Matrix — CJ_OS

**Versión:** 0.1.0  
**Fecha:** 2026-06-25  
**Estado:** Documento derivado — se regenera tras cada KES  
**Propósito:** Trazar cada elemento de conocimiento desde su definición hasta los documentos y componentes que lo usan. Si un elemento cambia, esta matriz indica dónde hay impacto.

---

## 1. Principio fundamental

> **Nada debe quedar huérfano. Todo concepto debe saberse de dónde viene y para qué se usa.**

La matriz evita que un cambio en un término, objeto o evento rompa documentos, reglas, decisiones o automatizaciones sin que se note.

---

## 2. Plantilla

| Elemento | Tipo | Definido en | Validado en | Lo usan |
|----------|------|-------------|-------------|---------|
| Vale | Término | Business Dictionary | KES-0 | Operating Model, Ontología, Event Catalog, Rules Catalog, Decision Catalog, PostgreSQL |
| Producto | Objeto | Ontología | KES-01 | Operating Model, Event Catalog, Knowledge Graph, PostgreSQL |

---

## 3. Matriz inicial

| Elemento | Tipo | Definido en | Validado en | Lo usan |
|----------|------|-------------|-------------|---------|
| **Vale** | Término | Business Dictionary | KES-0 | Operating Model, Ontología, Event Catalog, Rules Catalog, Decision Catalog, PostgreSQL |
| **Solicitud** | Término | Business Dictionary | KES-0 | Operating Model, Decision Catalog |
| **Pedido** | Término | Business Dictionary | KES-0 | Operating Model, Event Catalog, Decision Catalog |
| **Orden de compra** | Término | Business Dictionary | KES-0 | Operating Model, Event Catalog, Ontología |
| **Entrada** | Término / Evento | Business Dictionary / Event Catalog | KES-01 | Operating Model, Ontología, Rules Catalog, Automatización |
| **Recepción** | Proceso | Operating Model | KES-01 | Event Catalog, Rules Catalog, Decision Catalog |
| **Surtido** | Proceso | Operating Model | KES-01 | Event Catalog, Decision Catalog |
| **Embarque** | Proceso | Operating Model | KES-03 | Event Catalog, Logística |
| **Existencia** | Objeto | Ontología | KES-01 | Operating Model, Event Catalog, Knowledge Graph, PostgreSQL |
| **Stock** | Término | Business Dictionary | KES-0 | Operating Model, Ontología, SAE |
| **Producto** | Objeto | Ontología | KES-01 | Operating Model, Event Catalog, Knowledge Graph, PostgreSQL |
| **Rack** | Objeto | Ontología | KES-01 | Operating Model, Knowledge Graph, PostgreSQL |
| **Merma** | Objeto / Evento | Ontología / Event Catalog | KES-01 | Operating Model, Decision Catalog, Rules Catalog |
| **Proveedor** | Objeto | Ontología | KES-02 | Operating Model, Compras |
| **Cliente** | Objeto | Ontología | KES-05 | Operating Model, Ventas |
| **llego_mercancia** | Evento | Event Catalog | KES-01 | Operating Model, Automatización, n8n |
| **se_creo_vale** | Evento | Event Catalog | KES-01 | Operating Model, Rules Catalog, Automatización |
| **se_detecto_merma** | Evento | Event Catalog | KES-01 | Decision Catalog, Rules Catalog |
| **Nunca existencia negativa** | Regla | Rules Catalog | KES-01 | Cognitive Model, PostgreSQL |
| **No modificar vale cerrado** | Regla | Rules Catalog | KES-01 | Event Catalog, Cognitive Model |
| **Toda merma requiere evidencia** | Regla | Rules Catalog | KES-01 | Decision Catalog, Cognitive Model |
| **¿Aceptar recepción completa?** | Decisión | Decision Catalog | KES-01 | Operating Model, Cognitive Model |
| **¿Aplicar merma?** | Decisión | Decision Catalog | KES-01 | Rules Catalog, Cognitive Model |

---

## 4. Reglas de uso

1. **Cada elemento nuevo de conocimiento debe agregarse a esta matriz.**
2. **Si un elemento cambia, se revisan todos los documentos que lo usan.**
3. **Si un elemento no tiene definición o validación, no puede usarse en documentos derivados.**
4. **La matriz se actualiza automáticamente como parte de la consolidación de cada KES.**

---

## 5. Relación con el Definition of Done

Un elemento solo se considera "terminado" cuando:

- Está definido en un documento maestro.
- Está validado en una KES.
- Aparece en la Traceability Matrix.
- No genera inconsistencias con otros elementos.

---

## Historial de cambios

| Fecha | Versión | Cambio |
|-------|---------|--------|
| 2026-06-25 | 0.1.0 | Creación de la Traceability Matrix con plantilla y elementos iniciales de Almacén, Compras, Ventas y Logística. |
