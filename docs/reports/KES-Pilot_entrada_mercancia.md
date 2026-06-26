# KES-Pilot — Entrada de mercancía de proveedor

**Fecha:** 2026-06-26  
**Sesión:** KES-Pilot (validación metodológica)  
**Proceso:** Entrada de mercancía de proveedor  
**Dominio:** Almacén / Compras / Calidad  
**Participantes sugeridos:** Carlos, Salvador (Jefe de Almacén), Francisco (Auxiliar de Almacén), Comprador, Inspector de Calidad (si aplica).  
**Duración objetivo:** 30–45 minutos  
**Estado:** 🔄 Propuesta — pendiente de ejecución

---

## 1. Objetivo de la KES-Pilot

Validar que la metodología CJ_OS de extracción de conocimiento puede modelar un proceso real de 3P en 30–45 minutos, llenando todos los artefactos requeridos:

- Objetos (entidades)
- Eventos
- Proceso con 5 preguntas
- Reglas
- Decisiones
- Excepciones
- KPIs
- Pregunta de sabiduría

Si algo no tiene lugar, se ajusta la metodología antes de KES-0.

---

## 2. Proceso seleccionado

**Entrada de mercancía de proveedor** — desde que el transporte llega al almacén hasta que la mercancía queda registrada en inventario.

Se eligió porque:
- Es un proceso diario en 3P.
- Cruza tres áreas: Compras (OC), Almacén (recepción), Calidad (inspección).
- Tiene reglas claras y excepciones frecuentes.
- Ya existe documentación previa: `workspace/shared/kes_notes/PR-ALM-001-V3_Recepcion_Mercancia.txt`.

---

## 3. Actores

| Rol | Responsabilidad en este proceso |
|-----|----------------------------------|
| **Proveedor** | Entrega mercancía con documentación. |
| **Transportista** | Lleva la mercancía física. |
| **Logística** | Notifica arribo, coordina con proveedor. |
| **Jefe de Almacén** | Supervisa recepción, autoriza desviaciones. |
| **Auxiliar de Almacén** | Recibe, cuenta, inspecciona, registra. |
| **Comprador** | Resuelve discrepancias con proveedor. |
| **Inspector de Calidad** | Verifica conformidad si aplica. |

---

## 4. Objetos / entidades involucradas

| Entidad | Uso en este proceso |
|---------|---------------------|
| `Orden de compra (OC)` | Documento base contra el que se recibe. |
| `Factura del proveedor` | Evidencia fiscal y de contenido. |
| `Nota de remisión / carta porte` | Documento de transporte. |
| `Producto` | Lo que se recibe. |
| `Rack / Ubicación` | Donde se coloca temporalmente. |
| `Existencia` | Stock que se actualizará. |
| `Vale` | Movimiento de entrada formal. |
| `Evidencia fotográfica` | Fotos de empaque, daños, discrepancias. |
| `No conformidad` | Si la mercancía no cumple estándar. |
| `Merma` | Si se rechaza o daña material. |

---

## 5. Eventos identificados

| Evento | Significado |
|--------|-------------|
| `llego_mercancia` | El transporte está en almacén. |
| `se_inicio_recepcion` | Auxiliar comienza revisión documental. |
| `se_detecto_desfase` | Cantidad o producto no coincide con OC. |
| `se_detecto_dano` | Empaque o contenido dañado. |
| `mercancia_aprobada` | Pasa inspección y se autoriza entrada. |
| `mercancia_rechazada` | No se acepta; genera merma o devolución. |
| `se_genero_vale_entrada` | Entrada formal al almacén. |
| `se_actualizo_existencia` | Stock disponible actualizado. |

---

## 6. Proceso detallado (AS-IS)

### P1 — Notificación de arribo

| Pregunta | Respuesta |
|----------|-----------|
| ¿Qué lo inicia? | Proveedor confirma envío → Logística notifica. |
| ¿Qué lo termina? | Jefe de Almacén sabe que llegará mercancía. |
| ¿Qué información consume? | OC, proveedor, cantidad estimada, fecha/hora. |
| ¿Qué información produce? | Notificación interna (correo/mensaje). |
| ¿Qué evento genera? | `llego_mercancia` |

### P2 — Verificación documental

| Pregunta | Respuesta |
|----------|-----------|
| ¿Qué lo inicia? | Llegada del transporte. |
| ¿Qué lo termina? | Documentos validados o falta documentada. |
| ¿Qué información consume? | Factura, nota de remisión, OC. |
| ¿Qué información produce? | Registro de documentos recibidos / faltantes. |
| ¿Qué evento genera? | `se_inicio_recepcion` |

### P3 — Inspección física

| Pregunta | Respuesta |
|----------|-----------|
| ¿Qué lo inicia? | Documentos completos. |
| ¿Qué lo termina? | Conteo físico e inspección de empaque realizados. |
| ¿Qué información consume? | OC, factura, producto físico. |
| ¿Qué información produce? | Conteo real, evidencia fotográfica, checklist. |
| ¿Qué evento genera? | `mercancia_aprobada` o `se_detecto_desfase` / `se_detecto_dano` |

### P4 — Decisión de aceptación

| Pregunta | Respuesta |
|----------|-----------|
| ¿Qué lo inicia? | Resultado de inspección física. |
| ¿Qué lo termina? | Decisión: aceptar, aceptar con nota, rechazar. |
| ¿Qué información consume? | Discrepancias, daños, evidencia. |
| ¿Qué información produce? | Decisión documentada, correo a compras/logística. |
| ¿Qué evento genera? | `mercancia_aprobada` / `mercancia_rechazada` |

### P5 — Entrada a inventario

| Pregunta | Respuesta |
|----------|-----------|
| ¿Qué lo inicia? | Aprobación de recepción. |
| ¿Qué lo termina? | Mercancía en ubicación temporal o definitiva. |
| ¿Qué información consume? | Productos, cantidades, ubicación destino. |
| ¿Qué información produce? | Vale de entrada, actualización de existencias. |
| ¿Qué evento genera? | `se_genero_vale_entrada`, `se_actualizo_existencia` |

---

## 7. Reglas del proceso

| # | Regla | Tipo | ¿Se puede romper? | Quién autoriza excepción |
|---|-------|------|-------------------|--------------------------|
| R1 | Toda entrada requiere OC o autorización previa. | Integridad | No | — |
| R2 | La cantidad recibida debe coincidir con factura/remisión. | Integridad | Con nota | Jefe de Almacén + Compras |
| R3 | Producto dañado no entra a inventario. | Calidad | Solo con excepción documentada | Jefe de Almacén + Calidad |
| R4 | Toda discrepancia requiere evidencia fotográfica. | Flujo | No | — |
| R5 | Vale de entrada se genera solo después de aprobación. | Flujo | No | — |

---

## 8. Excepciones frecuentes

| Excepción | Causa | Acción |
|-----------|-------|--------|
| Mercancía sin OC | Error de proveedor o compras urgentes | Detener, notificar a Compras, esperar autorización. |
| Cantidad mayor a lo pedido | Error de surtido del proveedor | Aceptar solo con nota y autorización; rechazar excedente. |
| Producto dañado en tránsito | Transporte deficiente | Tomar evidencia, separar, gestionar con proveedor/seguro. |
| Producto no coincide con OC | Error de proveedor | Detener, documentar, esperar instrucciones de Compras. |
| Falta certificado de calidad | Documentación incompleta | Registrar observación, notificar, condicionar entrada. |

---

## 9. Decisiones clave

| Decisión | Información necesaria | Opciones | Responsable |
|----------|----------------------|----------|-------------|
| ¿Aceptar mercancía con discrepancia? | Evidencia, monto, impacto | Aceptar con nota / Rechazar / Aceptar condicional | Jefe de Almacén + Compras |
| ¿Ingresar material sin OC? | Urgencia, autorización por escrito | Sí, con autorización / No | Director / Compras |
| ¿Aplicar merma? | Cantidad dañada, causa, evidencia | Sí / No | Jefe de Almacén + Calidad |
| ¿Ubicar en zona de cuarentena? | Estado de inspección | Sí / No | Inspector de Calidad |

---

## 10. KPIs propuestos

| KPI | Meta | Fuente |
|-----|------|--------|
| Recepciones conformes | ≥ 98% | Reportes de recepción |
| Tiempo promedio de recepción | ≤ 2 horas | Timestamp de eventos |
| Precisión documental | 100% | Checklist de documentos |
| Mermas por recepción | < 1% | Registros de merma |

---

## 11. Pregunta de sabiduría

> **Si mañana contrataras a un nuevo gerente de almacén, ¿qué le explicarías sobre la recepción de mercancía que no aparece en ningún procedimiento escrito?**

Ejemplos de respuestas esperadas:
- Cómo identificar un proveedor problemático antes de que llegue la mercancía.
- Cuándo es mejor aceptar con nota y cuándo es mejor rechazar.
- Cómo negociar con transportistas para minimizar daños.

---

## 12. Resultados esperados de la KES-Pilot

Al finalizar la sesión se debe tener:

1. Confirmación de que la estructura de ficha maestra funciona.
2. Lista de términos que deben ir al Business Dictionary.
3. Identificación de reglas faltantes o contradictorias.
4. Confirmación de que el proceso genera eventos claros.
5. Decisión: ¿la metodología está lista para KES-0 o necesita ajustes?

---

## 13. Ajustes metodológicos pendientes

Después de la KES-Pilot, registrar aquí cualquier cambio necesario en:

- Estructura de la ficha maestra.
- Business Dictionary.
- Ontología.
- Knowledge Coverage Matrix.
- Protocolo KES.

________________________________________________________________________

________________________________________________________________________

---

*Documento generado por Kimi el 2026-06-26 como propuesta de KES-Pilot.*
