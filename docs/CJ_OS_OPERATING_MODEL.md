# Modelo Operativo de la Empresa — CJ_OS

**Versión:** 0.5.0  
**Fecha:** 2026-06-25  
**Estado:** Borrador base listo — M2.8 BKA/KES en preparación  
**Propósito:** Adquirir, documentar y validar el conocimiento empresarial de 3P antes de diseñar el Modelo de Datos (M3).

---

## 1. Relación con el resto de la arquitectura

Este documento es la **memoria semántica** de CJ_OS. Traduce la arquitectura funcional del `docs/CJ_OS_BLUEPRINT.md` y el ADN del `docs/CJ_OS_PHILOSOPHY.md` en el conocimiento operativo concreto de 3P.

```text
CJ_OS_BLUEPRINT.md      → Qué es el sistema y cómo está construido.
CJ_OS_PHILOSOPHY.md     → Cómo debe comportarse el sistema.
CJ_OS_OPERATING_MODEL.md → Qué sabe CJ_OS sobre 3P y cómo debe operarla.
```

> **Restricción vigente:** No se crearán tablas, APIs, módulos ni código hasta que el Blueprint, este Modelo Operativo, los catálogos de conocimiento y la Fase de Adquisición del Conocimiento Empresarial (M2.8 BKA/KES) sean aprobados por Carlos.

---

## 2. Enfoque: adquirir el conocimiento empresarial

Hasta ahora diseñamos la infraestructura y la arquitectura. A partir de este punto diseñamos el **conocimiento de CJ_OS**. Esa es la parte que más valor tendrá y la que será más difícil de copiar.

### Meta explícita del proyecto

> **Separar completamente el motor de CJ_OS del conocimiento específico de cada empresa.**

El Core (eventos, decisiones, memoria, agentes, seguridad, auditoría) debe ser genérico y reutilizable. Lo único que cambiará de una empresa a otra será el conocimiento del negocio.

### Metodología CJ_OS Framework

```text
CJ_OS Framework
       │
       ▼
Blueprint
       │
       ▼
Business Ontology
       │
       ▼
Operating Model
       │
       ▼
Knowledge Graph
       │
       ▼
Decision Catalog
       │
       ▼
Business Rules
       │
       ▼
Event Catalog
       │
       ▼
Data Model
       │
       ▼
Automation
       │
       ▼
AI
```

### Documentos de conocimiento

| Documento | Propósito |
|-----------|-----------|
| `docs/CJ_OS_FRAMEWORK.md` | Metodología reutilizable de implementación. |
| `docs/CJ_OS_ONTOLOGY.md` | Qué entidades existen, atributos, restricciones. |
| `docs/CJ_OS_KNOWLEDGE_GRAPH.md` | Cómo se relacionan las entidades. |
| `docs/CJ_OS_DECISION_CATALOG.md` | Qué decisiones se toman, quién las toma, con qué información. |
| `docs/CJ_OS_RULES_CATALOG.md` | Reglas de negocio accionables. |
| `docs/CJ_OS_EVENT_CATALOG.md` | Eventos que alimentan el sistema. |
| `docs/CJ_OS_OPERATING_MODEL.md` | Conocimiento operativo completo por dominio. |

### Tres versiones de cada dominio

Cada ficha maestra documenta tres estados:

1. **AS-IS (Estado actual):** ¿cómo trabaja la empresa hoy?
2. **TO-BE (Estado ideal):** ¿cómo debería trabajar con CJ_OS en un año?
3. **Automatización futura:** ¿qué hará CJ_OS automáticamente?

Esto da una visión de evolución, no solo de documentación.

### Todo vive por eventos

CJ_OS es una plataforma **event-driven**. Cada acción importante genera un evento:

```text
llego_mercancia
se_creo_vale
se_detecto_merma
se_cerro_inventario
stock_bajo_detectado
```

Los eventos alimentan el Event Bus, los workflows de n8n, los agentes de IA, los logs de auditoría y las automatizaciones.

---

## 3. Estructura de la ficha maestra por dominio

Cada dominio se documentará con la siguiente estructura estándar:

1. **Objetivo** — ¿para qué existe el dominio?
2. **AS-IS** — ¿cómo funciona hoy?
3. **TO-BE** — ¿cómo funcionará con CJ_OS?
4. **Automatización futura** — ¿qué hará CJ_OS solo?
5. **Actores** — ¿quién participa?
6. **Objetos** — ¿qué entidades existen y qué atributos tienen?
7. **Eventos** — ¿qué cosas pueden ocurrir?
8. **Procesos** — cada proceso responde 5 preguntas:
   - ¿Qué lo inicia?
   - ¿Qué lo termina?
   - ¿Qué información consume?
   - ¿Qué información produce?
   - ¿Qué evento genera?
9. **Reglas** — ¿qué nunca debe violarse?
10. **Lo que CJ_OS debe saber** — conocimiento semántico del dominio.
11. **Excepciones** — ¿qué pasa cuando algo falla?
12. **Decisiones** — ¿quién decide qué?
13. **KPIs** — ¿cómo medimos el desempeño?
14. **Matriz de madurez** — documentado, estandarizado, automatizable, automatizado.
15. **Pregunta final** — *¿Qué haría el mejor gerente de esta área que hoy nadie hace?*

---

## 4. Dominios funcionales de 3P

| ID | Dominio | Objetivo principal |
|----|---------|--------------------|
| D1 | **Dirección** | Definir objetivos, gobernar el SGC y tomar decisiones estratégicas. |
| D2 | **Ventas** | Convertir oportunidades en pedidos facturados y clientes satisfechos. |
| D3 | **Compras** | Asegurar el abastecimiento correcto, a tiempo y al mejor costo. |
| D4 | **Almacén** | Garantizar que siempre exista material correcto, identificado y disponible para surtido. |
| D5 | **Logística** | Entregar la mercancía al cliente de forma segura, puntual y trazable. |
| D6 | **Calidad** | Asegurar que productos y procesos cumplan estándares y mejoren continuamente. |
| D7 | **Contabilidad** | Registrar, controlar y reportar el flujo de dinero de la empresa. |
| D8 | **RRHH** | Administrar el talento, asistencia, capacitación y documentación del personal. |
| D9 | **Inteligencia Empresarial** | Convertir datos operativos en información útil para la toma de decisiones. |

### Dominios habilitadores del sistema

| ID | Dominio | Responsabilidad |
|----|---------|-----------------|
| D10 | **Automatización / Tecnología** | Workflows, conectores, n8n, reglas del Core, agentes de IA. |
| D11 | **Infraestructura / Seguridad** | Docker, PostgreSQL, Redis, backups, credenciales, accesos, logs. |

---

## 5. Roles definidos

| Rol | Descripción | Dominios principales |
|-----|-------------|----------------------|
| **Director (Carlos)** | Toma decisiones estratégicas, aprueba inversiones y define políticas. | D1, D7, D9, D10, D11 |
| **Gerente Comercial** | Gestiona clientes, cotizaciones, pedidos y equipo de ventas. | D2 |
| **Ejecutivo de Ventas** | Atiende clientes, genera cotizaciones y da seguimiento a pedidos. | D2 |
| **Comprador** | Gestiona proveedores, cotizaciones de compra y órdenes de compra. | D3 |
| **Jefe de Almacén (ej. Salvador)** | Controla inventario, ubicaciones, entradas, salidas e inventarios físicos. | D4 |
| **Auxiliar de Almacén (ej. Francisco)** | Recibe, acomoda, surte, cuenta y registra movimientos de mercancía. | D4 |
| **Coordinador de Logística** | Planea envíos, rutas y seguimiento de entregas. | D5 |
| **Operador de Logística** | Ejecuta empaque, etiquetado, carga y entregas. | D5 |
| **Jefe de Calidad (ej. Ernesto)** | Define criterios de inspección, gestiona no conformidades y acciones correctivas. | D6, D1 (SGC) |
| **Inspector de Calidad** | Realiza inspecciones y registra evidencia. | D6 |
| **Contador / Administrador** | Facturación, pagos, nómina, reportes financieros. | D7, D8 (nómina) |
| **Jefe de RRHH** | Administra personal, asistencia, capacitación y documentación interna. | D8 |
| **Analista de Inteligencia Empresarial** | Genera reportes, KPIs y análisis para la toma de decisiones. | D9 |
| **Responsable SGC** | Mantiene documentación ISO, auditorías e indicadores. | D1, D6 |
| **Sistemas / CJ_OS Admin** | Configura conectores, flujos, seguridad y permisos del sistema. | D10, D11 |
| **CJ_OS (agente digital)** | Asiste, automatiza, propone y escala según nivel de autonomía. | Todos (bajo supervisión) |

---

## 6. Niveles de autonomía A0-A5

| Nivel | Nombre | Descripción | Ejemplo |
|-------|--------|-------------|---------|
| **A0** | **Solo informar** | Muestra datos, alertas o estado. No decide. | "El stock de tornillos es 45. El mínimo es 100." |
| **A1** | **Recomendar** | Sugiere una acción. El humano decide. | "Recomiendo reordenar 200 tornillos con Proveedor A." |
| **A2** | **Ejecutar tareas reversibles** | Actúa solo en acciones de bajo impacto o reversibles. | Registrar un movimiento con escaneo. Enviar cotización de borrador. |
| **A3** | **Ejecutar procesos autorizados** | Ejecuta procesos previamente aprobados dentro de reglas claras. | Generar OC de reposición automática con proveedor y presupuesto autorizados. |
| **A4** | **Requiere aprobación humana** | Detiene la acción y pide confirmación. | Ajustar inventario por merma. Cancelar pedido. |
| **A5** | **Nunca permitido** | Nunca ejecuta. Solo informa o escala. | Eliminar vale cerrado. Emitir pago. Borrar auditoría. |

---

## 7. Fichas maestras por dominio

---

### D4 — Almacén (ficha patrón)

#### Objetivo

> Garantizar que siempre exista material correcto, identificado y disponible para surtido.

#### AS-IS — Estado actual

```text
Proveedor llega
  │
  ▼
Francisco recibe mercancía
  │
  ▼
Revisa físicamente
  │
  ▼
Si hay diferencias, avisa a Salvador / Compras
  │
  ▼
Captura en SAE
  │
  ▼
Actualiza Excel de almacén
  │
  ▼
Acomoda en rack
  │
  ▼
Registra evidencia (cuando aplica)
```

#### TO-BE — Estado ideal (con CJ_OS)

```text
Proveedor llega
  │
  ▼
CJ_OS reconoce la OC y el proveedor
  │
  ▼
Francisco confirma cantidad y condición
  │
  ▼
CJ_OS valida contra OC y alerta diferencias
  │
  ▼
Francisco captura con escaneo o voz
  │
  ▼
CJ_OS actualiza inventario en tiempo real
  │
  ▼
CJ_OS genera evidencia fotográfica vinculada
  │
  ▼
CJ_OS actualiza KPIs y notifica a Compras/Calidad/Ventas
```

#### Automatización futura

- Detectar stock bajo y sugerir compra.
- Comparar proveedores y recomendar el mejor.
- Crear OC de reposición y esperar aprobación.
- Enviar OC al proveedor y registrar seguimiento.
- Validar vales antes de cerrar.
- Generar inventarios cíclicos sugeridos.
- Detectar productos sin movimiento.
- Recomendar reubicaciones para reducir recorridos.
- Identificar patrones de mermas.
- Predecir quiebres de stock considerando estacionalidad.

#### Actores

| Actor | Rol en el dominio | Ejemplos reales en 3P |
|-------|-------------------|-----------------------|
| **Auxiliar de Almacén** | Recibe, acomoda, surte, cuenta y registra movimientos. | Francisco |
| **Jefe de Almacén** | Supervisa, autoriza ajustes, valida inventarios, decide excepciones. | Salvador |
| **Comprador** | Solicita recepción contra OC, resuelve discrepancias con proveedores. | — |
| **Calidad** | Inspecciona mercancía, retiene lotes, aprueba/rechaza entradas. | Ernesto |
| **Ventas** | Consulta disponibilidad, notifica pedidos listos, solicita reservas. | — |
| **Logística** | Retira mercancía surtida para entrega. | — |
| **CJ_OS** | Registra, alerta, propone, valida y audita. | — |

#### Objetos

| Objeto | Atributos clave | Relación con otros objetos |
|--------|-----------------|----------------------------|
| **Producto** | SKU, descripción, familia, proveedor principal, costo, precio, fotografía, manual, unidad de medida, peso, dimensiones. | Tiene existencia, ubicación, movimientos. |
| **Existencia** | Cantidad física, cantidad comprometida, cantidad disponible, stock mínimo, stock máximo, punto de reorden. | Pertenece a un producto en una ubicación. |
| **Ubicación / Rack** | Código, pasillo, nivel, zona, capacidad, tipo. | Contiene productos. |
| **Vale** | Tipo, folio, fecha, responsable, estado, líneas, motivo, evidencias. | Vinculado a productos, pedidos, OC, proveedor, cliente. |
| **Orden de Compra (OC)** | Folio, proveedor, fecha, estado, líneas, cantidad pedida/recibida. | Genera entradas de almacén. |
| **Pedido** | Folio, cliente, estado, líneas, reservas. | Genera salidas de almacén. |
| **Inventario / Conteo** | Tipo, fecha, responsable, estado, diferencias, ajustes. | Afecta existencias. |
| **Merma** | Producto, cantidad, causa, evidencia, responsable, aprobación, estado. | Genera ajuste de existencia. |
| **Transferencia** | Origen, destino, producto, cantidad, responsable, estado. | Mueve existencia entre ubicaciones. |
| **Material indirecto** | SKU, descripción, familia, stock, ubicación, responsable, consumo. | No se vende, se consume en operación. |
| **Evidencia fotográfica** | Imagen, fecha, usuario, evento asociado. | Vinculada a vales, mermas, inventarios. |

#### Eventos

| Evento | Descripción | Disparador típico |
|--------|-------------|-------------------|
| `llego_mercancia` | Un proveedor entrega mercancía en almacén. | OC autorizada, camión en rampa. |
| `se_creo_vale` | Se genera un vale. | Recepción, surtido, conteo, merma. |
| `se_modifico_vale` | Se edita un vale. | Corrección, autorización. |
| `se_cerro_vale` | El vale queda registrado y afecta existencias. | Validación final. |
| `se_cerro_inventario` | Un conteo físico se cierra. | Fin de conteo. |
| `se_detecto_merma` | Se encuentra producto dañado, caducado o faltante. | Inspección, conteo, devolución. |
| `se_tomo_fotografia` | Se captura evidencia fotográfica. | Entrada, merma, ubicación, daño. |
| `se_creo_oc` | Compras genera una OC. | Stock bajo, pedido de cliente. |
| `se_recibio_oc` | Se confirma recepción completa o parcial. | Entrada de mercancía. |
| `se_termino_surtido` | Se completa el picking de un pedido. | Pedido autorizado. |
| `se_imprimio_vale` | Se imprime o exporta un vale. | Cierre de vale. |
| `stock_bajo_detectado` | Producto en o bajo punto de reorden. | Scheduler o salida. |
| `stock_negativo_detectado` | Existencia negativa detectada. | Validación de regla. |

#### Procesos

Cada proceso responde cinco preguntas:

1. **¿Qué lo inicia?**
2. **¿Qué lo termina?**
3. **¿Qué información consume?**
4. **¿Qué información produce?**
5. **¿Qué evento genera?**

##### P1 — Entrada de mercancía

| Pregunta | Respuesta |
|----------|-----------|
| ¿Qué lo inicia? | Evento `llego_mercancia` (proveedor entrega en rampa). |
| ¿Qué lo termina? | Existencia actualizada y vale de entrada cerrado. |
| ¿Qué información consume? | OC, proveedor, productos, cantidades, estándares de calidad. |
| ¿Qué información produce? | Vale de entrada, existencia actualizada, evidencia fotográfica, recepción de OC. |
| ¿Qué evento genera? | `se_creo_vale`, `se_recibio_oc`, `se_cerro_vale`, `se_tomo_fotografia`. |

##### P2 — Salida de mercancía

| Pregunta | Respuesta |
|----------|-----------|
| ¿Qué lo inicia? | Pedido autorizado o solicitud de consumo interno. |
| ¿Qué lo termina? | Mercancía entregada a logística o área solicitante; stock actualizado. |
| ¿Qué información consume? | Pedido, disponibilidad de stock, ubicaciones de picking. |
| ¿Qué información produce? | Vale de salida, picking, existencia actualizada, reservas liberadas. |
| ¿Qué evento genera? | `se_creo_vale`, `se_termino_surtido`, `se_cerro_vale`. |

##### P3 — Inventario físico

| Pregunta | Respuesta |
|----------|-----------|
| ¿Qué lo inicia? | Programación de conteo cíclico o general. |
| ¿Qué lo termina? | Inventario cerrado con ajustes aprobados. |
| ¿Qué información consume? | Existencia del sistema, conteo físico, ubicaciones. |
| ¿Qué información produce? | Diferencias, ajustes propuestos, informe de inventario. |
| ¿Qué evento genera? | `se_cerro_inventario`, `se_detecto_merma` (si aplica). |

##### P4 — Ajuste de inventario

| Pregunta | Respuesta |
|----------|-----------|
| ¿Qué lo inicia? | Diferencia detectada en conteo, merma o error de captura. |
| ¿Qué lo termina? | Ajuste aplicado y auditado. |
| ¿Qué información consume? | Causa, cantidad, ubicación, autorización. |
| ¿Qué información produce? | Vale de ajuste, existencia corregida, registro de auditoría. |
| ¿Qué evento genera? | `se_creo_vale`, `se_cerro_vale`. |

##### P5 — Merma

| Pregunta | Respuesta |
|----------|-----------|
| ¿Qué lo inicia? | Detección de producto dañado, caducado o no conforme. |
| ¿Qué lo termina? | Merma aprobada y existencia ajustada. |
| ¿Qué información consume? | Producto, cantidad, causa, evidencia fotográfica, responsable. |
| ¿Qué información produce? | Registro de merma, ajuste de existencia, alerta de patrón. |
| ¿Qué evento genera? | `se_detecto_merma`, `se_creo_vale`, `se_cerro_vale`. |

##### P6 — Transferencia entre ubicaciones

| Pregunta | Respuesta |
|----------|-----------|
| ¿Qué lo inicia? | Necesidad de mover producto (reabastecimiento, reorganización, rack dañado). |
| ¿Qué lo termina? | Producto confirmado en ubicación destino. |
| ¿Qué información consume? | Producto, origen, destino, cantidad, capacidad destino. |
| ¿Qué información produce? | Vale de transferencia, existencia por ubicación actualizada. |
| ¿Qué evento genera? | `se_creo_vale`, `se_cerro_vale`. |

##### P7 — Reabastecimiento de picking

| Pregunta | Respuesta |
|----------|-----------|
| ¿Qué lo inicia? | Ubicación de picking por debajo del mínimo. |
| ¿Qué lo termina? | Ubicación de picking surtida desde reserva. |
| ¿Qué información consume? | Stock en picking, stock en reserva, producto. |
| ¿Qué información produce? | Transferencia, existencia por ubicación actualizada. |
| ¿Qué evento genera? | `se_creo_vale`, `se_cerro_vale`, `stock_bajo_detectado`. |

##### P8 — Material indirecto

| Pregunta | Respuesta |
|----------|-----------|
| ¿Qué lo inicia? | Entrada de insumos o solicitud de consumo. |
| ¿Qué lo termina? | Consumo registrado y stock actualizado. |
| ¿Qué información consume? | SKU, cantidad, área solicitante, responsable. |
| ¿Qué información produce? | Vale de entrada/salida, consumo por área, alerta de stock mínimo. |
| ¿Qué evento genera? | `se_creo_vale`, `se_cerro_vale`, `stock_bajo_detectado`. |

##### P9 — Devoluciones

| Pregunta | Respuesta |
|----------|-----------|
| ¿Qué lo inicia? | Cliente devuelve mercancía o proveedor autoriza devolución. |
| ¿Qué lo termina? | Mercancía reingresada, creditada o enviada a merma. |
| ¿Qué información consume? | Pedido original, motivo, estado físico, política de devolución. |
| ¿Qué información produce? | Vale de entrada por devolución, nota de crédito, merma (si aplica). |
| ¿Qué evento genera? | `devolucion_iniciada`, `se_creo_vale`, `se_detecto_merma`. |

##### P10 — Auditoría 5S

| Pregunta | Respuesta |
|----------|-----------|
| ¿Qué lo inicia? | Programación de auditoría. |
| ¿Qué lo termina? | Hallazgos cerrados con evidencia. |
| ¿Qué información consume? | Checklist, zona, fecha, responsable. |
| ¿Qué información produce? | Resultado de auditoría, acciones correctivas, evidencia. |
| ¿Qué evento genera? | `auditoria_realizada`, `accion_correctiva_creada`. |

#### Reglas

1. Nunca permitir existencia negativa. (A5)
2. No modificar un vale cerrado. (A5)
3. No eliminar inventarios históricos. (A5)
4. Toda merma requiere evidencia fotográfica y causa documentada. (A4)
5. Toda entrada requiere vinculación a proveedor y/o OC. (A2/A3)
6. Toda salida requiere responsable y motivo. (A2/A3)
7. Toda modificación importante debe auditarse. (A2-A5)
8. Un producto no puede salir si no hay disponibilidad. (A5)
9. El stock comprometido no puede superar la existencia física. (A5)
10. Las ubicaciones de picking deben reabastecerse antes de agotarse. (A1/A2)
11. El material indirecto debe tener responsable y control de consumo. (A3)

#### Lo que CJ_OS debe saber

- Un producto puede existir en varios racks al mismo tiempo.
- Un rack tiene capacidad máxima y tipo de almacenamiento.
- No todos los productos pueden mezclarse (incompatibilidades, temperatura, fragilidad).
- Una merma nunca elimina el historial del movimiento original.
- Un vale cerrado nunca se modifica; se revierte con otro documento.
- Los materiales indirectos no afectan ventas, pero sí costos y disponibilidad operativa.
- Las fotografías pertenecen a movimientos, no son archivos sueltos.
- Una OC puede surtirse parcialmente.
- Un pedido puede dividirse en varias entregas.
- El stock comprometido reduce la disponibilidad pero no la existencia física.
- El mismo SKU puede tener diferentes costos según lote o proveedor.
- Las ubicaciones de picking son distintas de las ubicaciones de reserva.

#### Excepciones

| Situación | Respuesta esperada | Autonomía de CJ_OS |
|-----------|--------------------|--------------------|
| Llega mercancía sin OC | Detener recepción, notificar a Compras y Jefe de Almacén. | A1: sugiere posibles OC abiertas; A4: alerta. |
| Sobran piezas en la recepción | Registrar excedente, investigar causa, ajustar OC o devolver. | A4: propone ajuste. |
| Faltan piezas en la recepción | Registrar faltante, notificar proveedor, generar NC si aplica. | A4: propone acción. |
| Llega mercancía dañada | Tomar evidencia, retener lote, notificar a Calidad/Compras. | A2: guarda evidencia; A4: alerta. |
| Francisco está de vacaciones | Reasignar tareas a otro auxiliar con los mismos permisos. | A2: sugiere reasignación. |
| SAE está caído | Continuar operando con Excel/vales físicos y sincronizar después. | A1: propone modo offline; A0: alerta. |
| Excel de almacén falla | Usar CJ_OS como fuente de verdad temporal hasta recuperar Excel. | A1: propone respaldo. |
| Internet no funciona | Modo offline con sincronización posterior; no detener operación. | A1: activa modo offline. |
| Se rompe un rack | Bloquear ubicación, reubicar productos, generar orden de mantenimiento. | A4: propone reubicación. |
| Cliente devuelve mercancía | Recibir, inspeccionar, registrar devolución, decidir crédito o merma. | A4: propone destino. |

#### Decisiones

| Decisión | Opciones | Quién decide | Autonomía de CJ_OS |
|----------|----------|--------------|--------------------|
| ¿Aceptar recepción completa? | Aceptar / Parcial / Rechazar | Jefe de Almacén + Calidad | A1: recomienda. |
| ¿Retener lote por calidad? | Retener / Liberar | Jefe de Calidad | A4: propone retención. |
| ¿Aplicar merma? | Aplicar / Rechazar / Investigar | Jefe de Almacén / Director | A4: propone ajuste con evidencia. |
| ¿Reordenar producto? | Sí / No / Diferente cantidad | Comprador / Director | A1: recomienda OC. |
| ¿Cambiar ubicación de producto? | Mover / Dejar | Jefe de Almacén | A2/A3: ejecuta si es dentro de política. |
| ¿Cerrar inventario con diferencias? | Cerrar / Recontar / Investigar | Jefe de Almacén | A4: propone ajustes. |

#### KPIs

| KPI | Cómo se mide | Meta orientativa |
|-----|--------------|------------------|
| Precisión de inventario | % de coincidencia física vs. sistema | ≥ 98% |
| Rotación de inventario | Veces que se renueva el stock por período | Definir por familia |
| Faltantes de surtido | Pedidos no surtidos por falta de stock | Tendencia a la baja |
| Merma | % de merma sobre valor de inventario | ≤ objetivo definido |
| Tiempo promedio de surtido | Tiempo desde pedido autorizado a entrega a logística | Definir meta |
| Ocupación de rack | % de capacidad utilizada | Optimizar |
| Entradas sin OC | % de entradas sin OC | Tendencia a cero |

#### Matriz de madurez

| Proceso | Documentado | Estandarizado | Automatizable | Automatizado |
|---------|-------------|---------------|---------------|--------------|
| Entradas de mercancía | ✅ | ✅ | ✅ | ❌ |
| Salidas de mercancía | ✅ | ✅ | ✅ | ❌ |
| Inventarios físicos | ✅ | ⚠️ | ✅ | ❌ |
| Ajustes de inventario | ✅ | ⚠️ | ✅ | ❌ |
| Mermas | ⚠️ | ⚠️ | ✅ | ❌ |
| Transferencias | ✅ | ✅ | ✅ | ❌ |
| Máximos y mínimos | ❌ | ❌ | ✅ | ❌ |
| Material indirecto | ⚠️ | ❌ | ✅ | ❌ |
| Devoluciones | ⚠️ | ⚠️ | ✅ | ❌ |
| Auditorías 5S | ⚠️ | ❌ | ✅ | ❌ |

#### Pregunta final

> **¿Qué haría el mejor gerente de almacén que hoy nadie hace?**

Posibles respuestas a validar:

- Detectar productos que llevan meses sin movimiento.
- Recomendar reubicaciones para reducir recorridos.
- Identificar patrones de mermas por proveedor, producto o temporada.
- Detectar errores recurrentes de surtido.
- Predecir quiebres de stock con estacionalidad.
- Medir el desempeño del almacén con indicadores automáticos.
- Comparar tiempos de surtido por auxiliar sin ser invasivo.
- Sugerir lotes a enviar primero (FEFO/FIFO) automáticamente.

---

### D3 — Compras (ficha maestra resumida)

#### Objetivo
Asegurar el abastecimiento correcto, a tiempo y al mejor costo.

#### AS-IS
Solicitud de compra → cotización → selección de proveedor → OC manual → seguimiento por correo/teléfono → recepción en almacén.

#### TO-BE
CJ_OS detecta necesidad → sugiere proveedor → genera borrador de OC → Comprador valida → CJ_OS envía OC → seguimiento automático → alerta de retrasos.

#### Automatización futura
- Generar solicitudes de compra desde stock bajo o pedido de cliente.
- Comparar proveedores por precio, lead time y calidad histórica.
- Crear OC borrador y esperar aprobación.
- Enviar OC y registrar confirmación del proveedor.
- Alertar retrasos y sugerir proveedores alternativos.

#### Actores
Comprador, Director, Jefe de Almacén, Proveedor, CJ_OS.

#### Objetos
Proveedor, OC, Cotización de compra, Solicitud de compra, Recepción, Evaluación de proveedor.

#### Eventos
`stock_bajo_detectado`, `se_creo_solicitud_compra`, `se_creo_cotizacion`, `se_creo_oc`, `se_envio_oc`, `se_recibio_oc`, `proveedor_retrasado`, `se_evaluo_proveedor`.

#### Procesos
Solicitud, cotización, selección, OC, seguimiento, recepción, evaluación.

#### Reglas
- Toda OC requiere proveedor autorizado.
- OC mayor a umbral requiere aprobación de Director.
- No se cancela OC ya recibida.
- Toda recepción debe coincidir con OC o ser justificada.

#### Lo que CJ_OS debe saber
- Un proveedor puede tener múltiples contactos y condiciones comerciales.
- Una OC puede tener entregas parciales.
- El precio de compra puede variar por volumen, moneda o temporada.
- El lead time es diferente para cada proveedor/producto.

#### Excepciones
- Proveedor no cumple fecha de entrega.
- Producto recibido no coincide con OC.
- Precio de factura difiere de OC.
- Proveedor caído o fuera de línea.

#### Decisiones
- ¿Aprobar OC mayor a umbral? → Director.
- ¿Aceptar entrega parcial? → Jefe de Almacén + Comprador.
- ¿Cambiar de proveedor? → Comprador / Director.

#### KPIs
- Tiempo de respuesta de proveedores.
- % de entregas a tiempo.
- Costo de compra vs. presupuesto.
- Calidad de proveedor (NC por lote).

#### Matriz de madurez
| Proceso | Documentado | Estandarizado | Automatizable | Automatizado |
|---------|-------------|---------------|---------------|--------------|
| Solicitud de compra | ⚠️ | ❌ | ✅ | ❌ |
| Cotización | ✅ | ⚠️ | ✅ | ❌ |
| Generación de OC | ✅ | ✅ | ✅ | ❌ |
| Seguimiento | ⚠️ | ❌ | ✅ | ❌ |
| Evaluación de proveedores | ❌ | ❌ | ✅ | ❌ |

#### Pregunta final
> **¿Qué haría el mejor comprador que hoy nadie hace?**
> Ejemplo: Negociar automáticamente con proveedores alternativos ante un retraso.

---

### D5 — Logística (ficha maestra resumida)

#### Objetivo
Entregar la mercancía al cliente de forma segura, puntual y trazable.

#### AS-IS
Pedido listo → empaque manual → guía escrita o generada → entrega al transportista → seguimiento por teléfono o WhatsApp.

#### TO-BE
Pedido listo → CJ_OS agrupa por zona → asigna transportista → genera guía → registra despacho → rastreo automático → confirmación de entrega.

#### Automatización futura
- Agrupar pedidos por ruta óptima.
- Asignar transportista según costo, tiempo y confiabilidad.
- Generar guías automáticamente.
- Enviar notificación de envío al cliente.
- Rastrear entrega y alertar retrasos.

#### Actores
Coordinador de Logística, Operador, Transportista, Cliente, CJ_OS.

#### Objetos
Envío, Ruta, Guía, Transportista, Pedido, Empaque, Devolución.

#### Eventos
`pedido_listo_para_envio`, `se_genero_ruta`, `se_genero_guia`, `mercancia_despachada`, `entrega_confirmada`, `entrega_fallida`, `devolucion_iniciada`.

#### Procesos
Planeación de rutas, empaque, guías, despacho, seguimiento, confirmación, devoluciones.

#### Reglas
- No se envía sin pedido autorizado y surtido.
- Toda guía debe tener transportista asignado.
- Devolución requiere inspección en almacén.

#### Lo que CJ_OS debe saber
- Una ruta puede incluir múltiples pedidos.
- Un transportista puede tener múltiples vehículos.
- El costo de envío puede variar por zona, peso o volumen.
- Un pedido puede dividirse en varios envíos.

#### Excepciones
- Transportista no llega.
- Cliente no recibe.
- Mercancía dañada en tránsito.
- Dirección incorrecta.
- Devolución rechazada por cliente.

#### Decisiones
- ¿Asignar transportista X o Y? → Coordinador de Logística.
- ¿Dividir pedido en varios envíos? → Coordinador / Ventas.
- ¿Aceptar devolución? → Calidad / Almacén.

#### KPIs
- % de entregas a tiempo.
- Costo promedio de envío.
- Incidentes por transportista.
- Tiempo de tránsito promedio.

#### Matriz de madurez
| Proceso | Documentado | Estandarizado | Automatizable | Automatizado |
|---------|-------------|---------------|---------------|--------------|
| Planeación de rutas | ⚠️ | ❌ | ✅ | ❌ |
| Empaque | ✅ | ⚠️ | ✅ | ❌ |
| Generación de guías | ✅ | ✅ | ✅ | ❌ |
| Seguimiento | ⚠️ | ❌ | ✅ | ❌ |
| Devoluciones | ⚠️ | ⚠️ | ✅ | ❌ |

#### Pregunta final
> **¿Qué haría el mejor coordinador de logística que hoy nadie hace?**
> Ejemplo: Reprogramar rutas en tiempo real ante un incidente.

---

### D6 — Calidad (ficha maestra resumida)

#### Objetivo
Asegurar que productos y procesos cumplan estándares y mejoren continuamente.

#### AS-IS
Inspección manual → registro en papel/Excel → NC en correo → seguimiento informal → auditorías programadas manualmente.

#### TO-BE
CJ_OS programa inspecciones → registro digital con evidencia → NC automática → flujo de acción correctiva → alertas de vencimiento → dashboard de calidad.

#### Automatización futura
- Programar inspecciones según riesgo y historial.
- Detectar patrones de NC por proveedor/producto.
- Sugerir acciones correctivas basadas en casos previos.
- Alertar auditorías próximas a vencer.

#### Actores
Jefe de Calidad, Inspector, Jefe de Almacén, Proveedor, Responsable SGC, CJ_OS.

#### Objetos
Inspección, NC, AC, Estándar de calidad, Lote, Proveedor evaluado, Auditoría.

#### Eventos
`inspeccion_programada`, `lote_retenido`, `no_conformidad_detectada`, `accion_correctiva_creada`, `auditoria_realizada`, `lote_liberado`.

#### Procesos
Inspección de entrada, NC, análisis de causa, AC, control de proveedores, auditorías, 5S.

#### Reglas
- Lote retenido no se libera sin aprobación de Calidad.
- Toda NC requiere causa y AC.
- Auditorías deben programarse y cerrarse.

#### Lo que CJ_OS debe saber
- Un lote puede estar retenido, liberado o rechazado.
- Una NC puede ser interna o de proveedor.
- Una AC puede tardar días o semanas en cerrarse.
- El desempeño de un proveedor se mide por calidad, entrega y precio.

#### Excepciones
- Proveedor rechaza responsabilidad de NC.
- Lote retenido afecta pedido urgente.
- No hay estándar definido para un producto nuevo.
- Auditoría externa detecta hallazgo grave.

#### Decisiones
- ¿Liberar o retener lote? → Jefe de Calidad.
- ¿Aprobar acción correctiva? → Responsable SGC / Director.
- ¿Dar de baja a proveedor? → Director con datos de calidad.

#### KPIs
- % de lotes aceptados a primera inspección.
- Tiempo promedio de cierre de NC.
- NC por proveedor.
- Cumplimiento de programa de auditorías.

#### Matriz de madurez
| Proceso | Documentado | Estandarizado | Automatizable | Automatizado |
|---------|-------------|---------------|---------------|--------------|
| Inspecciones | ✅ | ✅ | ✅ | ❌ |
| No conformidades | ✅ | ⚠️ | ✅ | ❌ |
| Acciones correctivas | ✅ | ⚠️ | ✅ | ❌ |
| Auditorías | ✅ | ✅ | ✅ | ❌ |
| 5S | ⚠️ | ❌ | ✅ | ❌ |

#### Pregunta final
> **¿Qué haría el mejor jefe de calidad que hoy nadie hace?**
> Ejemplo: Predecir qué proveedor generará la próxima NC antes de que ocurra.

---

### D2 — Ventas (ficha maestra resumida)

#### Objetivo
Convertir oportunidades en pedidos facturados y clientes satisfechos.

#### AS-IS
Lead por WhatsApp/correo → cotización manual → seguimiento informal → pedido → reserva en Excel → facturación.

#### TO-BE
Lead entra → CJ_OS clasifica → genera cotización → seguimiento automático → pedido → reserva de stock → alerta de pedido listo → factura.

#### Automatización futura
- Clasificar leads y asignar ejecutivo.
- Sugerir precios y descuentos según política.
- Enviar seguimientos automáticos.
- Reservar stock al crear pedido.
- Alertar pedidos estancados.

#### Actores
Gerente Comercial, Ejecutivo, Cliente, Almacén, Contador, CJ_OS.

#### Objetos
Cliente, Lead, Cotización, Pedido, Descuento, Factura, Oportunidad.

#### Eventos
`nuevo_lead`, `cotizacion_creada`, `pedido_creado`, `pedido_autorizado`, `descuento_solicitado`, `pedido_facturado`, `queja_registrada`.

#### Procesos
Prospección, cotización, pedido, reserva, descuentos, facturación, postventa.

#### Reglas
- Pedido requiere cliente registrado.
- Descuento fuera de política requiere aprobación.
- No se factura sin stock comprometido o pedido autorizado.

#### Lo que CJ_OS debe saber
- Un cliente puede tener lista de precios especial.
- Un pedido puede tener múltiples entregas.
- Una cotización puede vencer.
- El stock comprometido no es lo mismo que el disponible.

#### Excepciones
- Cliente pide descuento fuera de política.
- No hay stock para cumplir fecha prometida.
- Cliente cancela pedido ya surtido.
- Queja grave de cliente.

#### Decisiones
- ¿Aprobar descuento especial? → Gerente Comercial / Director.
- ¿Reservar stock sin pago? → Política comercial.
- ¿Dividir pedido? → Ventas / Almacén.

#### KPIs
- Conversión de cotizaciones.
- Tiempo de respuesta a clientes.
- Pedidos entregados a tiempo.
- Quejas y devoluciones.

#### Matriz de madurez
| Proceso | Documentado | Estandarizado | Automatizable | Automatizado |
|---------|-------------|---------------|---------------|--------------|
| Prospección | ⚠️ | ❌ | ✅ | ❌ |
| Cotización | ✅ | ✅ | ✅ | ❌ |
| Pedido | ✅ | ✅ | ✅ | ❌ |
| Seguimiento | ❌ | ❌ | ✅ | ❌ |
| Postventa | ⚠️ | ❌ | ✅ | ❌ |

#### Pregunta final
> **¿Qué haría el mejor gerente comercial que hoy nadie hace?**
> Ejemplo: Identificar qué clientes están a punto de dejar de comprar.

---

### D7 — Contabilidad (ficha maestra resumida)

#### Objetivo
Registrar, controlar y reportar el flujo de dinero de la empresa.

#### AS-IS
Facturas en SAE → cobranza por correo/telefónica → pagos programados manualmente → nómina en software externo → reportes en Excel.

#### TO-BE
CJ_OS concilia facturas, alerta vencimientos, programa pagos, genera nómina desde asistencia y produce reportes ejecutivos automáticos.

#### Automatización futura
- Conciliar pagos recibidos contra facturas.
- Alertar facturas por vencer.
- Programar pagos a proveedores dentro de flujo aprobado.
- Generar reportes financieros periódicos.

#### Actores
Contador, Director, Comprador, Ejecutivo, CJ_OS.

#### Objetos
Factura, Pago, Cuenta por cobrar, Cuenta por pagar, Nómina, Estado financiero.

#### Eventos
`factura_emitida`, `pago_recibido`, `pago_programado`, `pago_realizado`, `nomina_generada`.

#### Procesos
Facturación, cobranza, pagos, nómina, estados financieros.

#### Reglas
- Egreso mayor a umbral requiere aprobación de Director.
- Toda factura se liga a pedido o servicio.
- Nómina requiere asistencia validada.

#### Lo que CJ_OS debe saber
- Una factura puede estar pagada, parcial o pendiente.
- Un cliente puede tener crédito o prepago.
- Un pago puede abonar varias facturas.
- Los impuestos dependen del producto, cliente y régimen.

#### Excepciones
- Cliente no paga a tiempo.
- Factura de proveedor no coincide con OC.
- Error en cálculo de nómina.
- Cambio de régimen fiscal.

#### Decisiones
- ¿Aprobar pago mayor a umbral? → Director.
- ¿Condonar mora? → Director.
- ¿Ajustar nómina? → Contador / Director.

#### KPIs
- Días promedio de cobro.
- Morosidad.
- Egresos vs. presupuesto.
- Costo de nómina.

#### Matriz de madurez
| Proceso | Documentado | Estandarizado | Automatizable | Automatizado |
|---------|-------------|---------------|---------------|--------------|
| Facturación | ✅ | ✅ | ✅ | ❌ |
| Cobranza | ✅ | ⚠️ | ✅ | ❌ |
| Pagos | ✅ | ✅ | ✅ | ❌ |
| Nómina | ✅ | ✅ | ✅ | ❌ |
| Reportes financieros | ⚠️ | ❌ | ✅ | ❌ |

#### Pregunta final
> **¿Qué haría el mejor contador que hoy nadie hace?**
> Ejemplo: Predecir problemas de flujo de efectivo 30 días antes.

---

### D8 — RRHH (ficha maestra resumida)

#### Objetivo
Administrar el talento, asistencia, capacitación y documentación del personal.

#### AS-IS
Alta en papel → asistencia manual o biométrico → permisos por correo → nómina en Excel/software externo → capacitaciones sin seguimiento.

#### TO-BE
CJ_OS centraliza expedientes, asistencia, permisos, vacaciones y capacitaciones; alerta vencimientos y genera reportes de desempeño.

#### Automatización futura
- Registrar asistencia automáticamente.
- Calcular días de vacaciones disponibles.
- Alertar vencimiento de capacitaciones.
- Generar reportes de ausentismo.

#### Actores
Jefe de RRHH, Empleado, Contador, Director, CJ_OS.

#### Objetos
Empleado, Expediente, Asistencia, Permiso, Vacación, Capacitación, Evaluación.

#### Eventos
`empleado_contratado`, `asistencia_registrada`, `permiso_solicitado`, `vacacion_aprobada`, `capacitacion_programada`.

#### Procesos
Alta/baja, asistencia, permisos, vacaciones, capacitación, evaluaciones.

#### Reglas
- Toda baja requiere aprobación.
- Modificación salarial requiere aprobación de Director.
- Documentación del empleado debe estar completa.

#### Lo que CJ_OS debe saber
- Un empleado puede tener múltiples roles.
- La asistencia afecta nómina.
- Las vacaciones se acumulan por antigüedad.
- Las capacitaciones pueden ser obligatorias.

#### Excepciones
- Empleado falta sin avisar.
- Permiso urgente fuera de horario.
- Documentación vencida.
- Incapacidad extendida.

#### Decisiones
- ¿Aprobar vacaciones? → Jefe de RRHH / Director.
- ¿Aumento salarial? → Director.
- ¿Baja de empleado? → Director.

#### KPIs
- Ausentismo.
- Rotación de personal.
- Capacitaciones completadas.
- Tiempo promedio de permanencia.

#### Matriz de madurez
| Proceso | Documentado | Estandarizado | Automatizable | Automatizado |
|---------|-------------|---------------|---------------|--------------|
| Expedientes | ✅ | ⚠️ | ✅ | ❌ |
| Asistencia | ✅ | ✅ | ✅ | ❌ |
| Permisos/vacaciones | ⚠️ | ⚠️ | ✅ | ❌ |
| Capacitaciones | ❌ | ❌ | ✅ | ❌ |
| Evaluaciones | ❌ | ❌ | ✅ | ❌ |

#### Pregunta final
> **¿Qué haría el mejor jefe de RRHH que hoy nadie hace?**
> Ejemplo: Detectar signos de desmotivación o rotación antes de que el empleado renuncie.

---

### D9 — Inteligencia Empresarial (ficha maestra resumida)

#### Objetivo
Convertir datos operativos en información útil para la toma de decisiones.

#### AS-IS
Reportes manuales en Excel, KPIs dispersos, decisiones basadas en percepción.

#### TO-BE
CJ_OS genera dashboards automáticos, alerta desviaciones, detecta tendencias y audita calidad de datos.

#### Automatización futura
- Generar reportes operativos diarios/semanales/mensuales.
- Alertar desviaciones de KPIs.
- Detectar inconsistencias en datos.
- Predecir demanda, morosidad, quiebres.

#### Actores
Analista, Director, Responsables de dominio, CJ_OS.

#### Objetos
Reporte, KPI, Alerta, Dashboard, Análisis de tendencia, Dato maestro.

#### Eventos
`reporte_solicitado`, `kpi_actualizado`, `alerta_generada`, `dashboard_publicado`, `inconsistencia_detectada`.

#### Procesos
Definición de indicadores, captura de datos, generación de reportes, análisis, auditoría de datos.

#### Reglas
- Un KPI debe tener dueño, frecuencia y meta.
- Alertas deben ser accionables.
- Datos maestros deben tener única fuente de verdad.

#### Lo que CJ_OS debe saber
- Un KPI puede depender de múltiples dominios.
- Los datos pueden tener lagunas o errores.
- Las predicciones mejoran con más historial.

#### Excepciones
- Dato maestro inconsistente entre sistemas.
- Reporte no generado por falla de conector.
- KPI sin dueño definido.

#### Decisiones
- ¿Aprobar nuevo KPI? → Director.
- ¿Cambiar meta de indicador? → Director con área dueña.

#### KPIs
- Tiempo de generación de reportes.
- % de decisiones basadas en datos.
- Calidad de datos (% de registros completos).

#### Matriz de madurez
| Proceso | Documentado | Estandarizado | Automatizable | Automatizado |
|---------|-------------|---------------|---------------|--------------|
| Definición de KPIs | ⚠️ | ❌ | ✅ | ❌ |
| Reportes operativos | ✅ | ⚠️ | ✅ | ❌ |
| Dashboards ejecutivos | ❌ | ❌ | ✅ | ❌ |
| Análisis predictivo | ❌ | ❌ | ✅ | ❌ |

#### Pregunta final
> **¿Qué haría el mejor analista de datos que hoy nadie hace?**
> Ejemplo: Predecir el impacto financiero de una decisión antes de tomarla.

---

### D1 — Dirección (ficha maestra resumida)

#### Objetivo
Definir objetivos, gobernar el SGC y tomar decisiones estratégicas.

#### AS-IS
Objetivos en reuniones, indicadores en Excel, decisiones basadas en experiencia.

#### TO-BE
CJ_OS consolida objetivos, KPIs, riesgos y decisiones en dashboards ejecutivos con alertas y proyecciones.

#### Automatización futura
- Consolidar reportes ejecutivos.
- Alertar riesgos y desviaciones.
- Registrar decisiones y sus razones.
- Preparar briefings para reuniones.

#### Actores
Director, Responsable SGC, Jefes de dominio, CJ_OS.

#### Objetos
Objetivo estratégico, Política, Indicador estratégico, Reporte ejecutivo, Decisión, Riesgo.

#### Eventos
`objetivo_definido`, `politica_aprobada`, `decision_tomada`, `riesgo_identificado`.

#### Procesos
Planeación estratégica, gobierno del SGC, aprobaciones mayores, revisión de indicadores.

#### Reglas
- Políticas solo las aprueba Dirección.
- Decisiones mayores deben quedar documentadas.
- Todo riesgo crítico debe tener plan de acción.

#### Lo que CJ_OS debe saber
- Los objetivos se descomponen en metas por dominio.
- Las políticas afectan a todos los dominios.
- Las decisiones del director tienen trazabilidad.

#### Excepciones
- Conflicto entre objetivos.
- Riesgo no previsto.
- Cambio regulatorio urgente.

#### Decisiones
- ¿Aprobar inversión? → Director.
- ¿Cambiar política comercial? → Director.
- ¿Escalar riesgo? → Director.

#### KPIs
- Cumplimiento de objetivos estratégicos.
- Tiempo de respuesta a decisiones críticas.
- Efectividad de acciones correctivas.

#### Matriz de madurez
| Proceso | Documentado | Estandarizado | Automatizable | Automatizado |
|---------|-------------|---------------|---------------|--------------|
| Objetivos estratégicos | ✅ | ⚠️ | ✅ | ❌ |
| Políticas | ✅ | ✅ | ✅ | ❌ |
| Reportes ejecutivos | ⚠️ | ❌ | ✅ | ❌ |
| Gestión de riesgos | ❌ | ❌ | ✅ | ❌ |

#### Pregunta final
> **¿Qué haría el mejor director de empresa que hoy nadie hace?**
> Ejemplo: Simular el impacto de diferentes escenarios antes de decidir.

---

## 8. Procesos transversales

### PT1 — Pedido completo

```text
Cliente
  │
  ▼
Ventas (cotización, pedido, reserva)
  │
  ▼
Almacén (validación de stock, picking, surtido)
  │
  ▼
Logística (empaque, guía, envío)
  │
  ▼
Contabilidad (factura, pago)
  │
  ▼
Cliente (entrega + factura)
```

### PT2 — Reabastecimiento de inventario

```text
Almacén (stock bajo)
  │
  ▼
Compras (OC)
  │
  ▼
Proveedor (entrega)
  │
  ▼
Almacén (recepción)
  │
  ▼
Calidad (inspección, si aplica)
  │
  ▼
Contabilidad (pago)
```

### PT3 — No conformidad

```text
Cualquier dominio (detección)
  │
  ▼
Calidad (registro, análisis de causa)
  │
  ▼
Dirección / Responsable SGC (aprobación de acción)
  │
  ▼
Dominio responsable (acción correctiva)
  │
  ▼
Calidad (cierre y evidencia)
```

### PT4 — Inteligencia / Reporte

```text
Inteligencia Empresarial (solicitud o programación)
  │
  ▼
Cada dominio (datos fuente)
  │
  ▼
Inteligencia Empresarial (procesamiento, análisis)
  │
  ▼
Dirección (revisión y decisión)
```

---

## 9. Plan de sesiones — M2.8 Business Knowledge Acquisition (BKA)

**Nombre:** Fase de Adquisición del Conocimiento Empresarial.

**Sesiones:** **Knowledge Engineering Sessions (KES)** / Sesiones de Ingeniería del Conocimiento (SIC).

**Objetivo:** Extraer conocimiento experto de cada área de 3P. No son entrevistas ni documentación pasiva. Son sesiones de extracción estructurada de conocimiento.

| KES/SIC | Dominio | Prioridad | Entregable |
|---------|---------|-----------|------------|
| 1 | **Almacén** | 🔴 Alta | Ficha maestra D4, tripletas de Knowledge Graph, eventos, decisiones y reglas validadas. |
| 2 | **Compras** | 🟡 Media | Ficha maestra D3 validada. |
| 3 | **Logística** | 🟡 Media | Ficha maestra D5 validada. |
| 4 | **Calidad** | 🟡 Media | Ficha maestra D6 validada. |
| 5 | **Ventas** | 🟡 Media | Ficha maestra D2 validada. |
| 6 | **Contabilidad** | 🟢 Baja | Ficha maestra D7 validada. |
| 7 | **RRHH** | 🟢 Baja | Ficha maestra D8 validada. |
| 8 | **Inteligencia Empresarial** | 🟡 Media | Ficha maestra D9 validada. |
| 9 | **Dirección y transversales** | 🔴 Alta | Ficha D1, procesos transversales y Modelo Operativo aprobado. |

> **Regla de la sesión:** Ningún dominio se da por adquirido si no quedan claros su AS-IS, TO-BE, automatización, conocimiento, excepciones, decisiones, reglas, eventos y matriz de madurez.

---

## 10. Flujos de decisión frecuentes

### FD1 — Foto de mercancía llega por WhatsApp
```text
1. Evento `se_tomo_fotografia`.
2. Core identifica remitente.
3. Memory busca OC o pedido relacionado.
4. Rules valida permisos del remitente.
5. Decision Engine:
   - Proveedor con OC abierta → A2/A3: guardar evidencia, notificar almacén.
   - Sin contexto → A1: "¿Esta foto corresponde a la OC #12345?"
   - Daño grave → A4/A5: alertar a Jefe de Calidad.
```

### FD2 — Stock bajo detectado
```text
1. Evento `stock_bajo_detectado`.
2. Knowledge: proveedor habitual, lead time, demanda.
3. Rules: ¿autorizado comprar hasta cierto monto?
4. Decision Engine:
   - A1: proponer OC al Comprador.
   - Monto > límite → A4: requerir aprobación de Director.
```

### FD3 — Vale con error detectado por Francisco
```text
1. Francisco reporta error.
2. CJ_OS verifica estado del vale:
   - No cerrado → A2: permitir corrección con trazabilidad.
   - Cerrado → A4: propone reversión a Jefe de Almacén.
   - Afectó facturación/entrega → A5: escala a Jefe de Almacén + Contabilidad.
```

---

## 11. Matriz RACI para decisiones clave

| Decisión / Tarea | Director | Gerente Comercial | Jefe Almacén | Comprador | Jefe Calidad | Contador | CJ_OS |
|------------------|----------|-------------------|--------------|-----------|--------------|----------|-------|
| Definir política de descuentos | A / R | C | I | I | I | I | I |
| Aprobar descuento excepcional | A | R | I | I | I | I | C |
| Generar cotización | I | A | I | I | I | I | R |
| Crear orden de compra | I | I | C | A / R | I | C | R |
| Aprobar OC mayor a límite | A | I | C | R | I | C | R |
| Registrar entrada de inventario | I | I | A | C | C | I | R |
| Retener lote por calidad | I | I | C | C | A / R | I | R |
| Aplicar merma / ajuste | A | I | R | I | C | I | C |
| Programar pago a proveedor | A | I | I | C | I | R | R |
| Generar reporte ejecutivo | A | C | C | C | C | C | R |
| Configurar conector / permiso | A | I | I | I | I | I | R |

**Leyenda:** R = Responsable, A = Aprobador, C = Consultado, I = Informado.

---

## 12. Criterios de aprobación del Modelo Operativo

Antes de iniciar M3 (Modelo de Datos), el conocimiento empresarial debe cumplir:

- [ ] `docs/CJ_OS_ONTOLOGY.md` tiene entidades, atributos y restricciones validadas.
- [ ] `docs/CJ_OS_KNOWLEDGE_GRAPH.md` tiene relaciones entre entidades validadas.
- [ ] `docs/CJ_OS_EVENT_CATALOG.md` tiene eventos nombrados y con payload definido.
- [ ] `docs/CJ_OS_DECISION_CATALOG.md` tiene decisiones con información, opciones y responsables.
- [ ] `docs/CJ_OS_RULES_CATALOG.md` tiene reglas con tipo, prioridad y evento relacionado.
- [ ] `docs/CJ_OS_OPERATING_MODEL.md` tiene fichas maestras completas por dominio.
- [ ] Cada dominio operativo (D1-D9) tiene AS-IS, TO-BE y automatización futura.
- [ ] Se documentó el conocimiento semántico en "Lo que CJ_OS debe saber".
- [ ] Se identificaron y documentaron las excepciones principales.
- [ ] Se construyó la matriz de madurez por dominio.
- [ ] Se respondió la pregunta final de cada KES/SIC.
- [ ] Las decisiones tienen actor responsable y nivel de autonomía A0-A5.
- [ ] Los procesos transversales están documentados.
- [ ] Carlos aprueba el conocimiento empresarial validado.

---

## 13. Notas de validación pendiente

> La ficha maestra de **Almacén** es el patrón. Las demás se completarán en las sesiones de BKA.
>
> Para validar Almacén con Carlos/Salvador/Francisco:
> 1. ¿El AS-IS refleja cómo trabajan hoy?
> 2. ¿El TO-BE es una visión realista para un año?
> 3. ¿Cada proceso responde las 5 preguntas correctamente?
> 4. ¿Faltan objetos o atributos clave?
> 5. ¿Las reglas son innegociables?
> 6. ¿Las excepciones cubren las situaciones reales?
> 7. ¿La matriz de madurez es honesta?
> 8. ¿Qué respuesta surge de la pregunta final?

---

## Historial de cambios

| Fecha | Versión | Cambio |
|-------|---------|--------|
| 2026-06-25 | 0.1.0 | Creación del Modelo Operativo como entregable M2.5. |
| 2026-06-25 | 0.2.0 | Reestructuración: dominios operativos de 3P, permisos granulares, autonomía A0-A5, procesos transversales y plan de sesiones M2.x. |
| 2026-06-25 | 0.3.0 | Adopción de fichas maestras por dominio. Ficha patrón de Almacén. |
| 2026-06-25 | 0.4.0 | Renombrado M2.x a Business Knowledge Acquisition (BKA). Fichas con AS-IS, TO-BE, automatización, conocimiento, excepciones, matriz de madurez y pregunta final. Meta de separación motor/conocimiento. |
| 2026-06-25 | 0.5.0 | Reorganización metodológica: sesiones renombradas a Knowledge Engineering Sessions (KES/SIC), procesos con 5 preguntas, integración con Ontología, Knowledge Graph, Catálogo de Eventos, Decisiones y Reglas. |
