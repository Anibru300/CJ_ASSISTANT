# Prebrief KES-Pilot — Almacén: Entrada de mercancía de proveedor

**Nota temporal.** Conocimiento extraído por pre-lectura de `PR-ALM-001-V3_Recepcion_Mercancia.docx` y `PR-ALM-002-V3_Ingreso_Almacen.docx`. Todo lo aquí anotado es **hipótesis a validar con el experto** durante la sesión KES-Pilot.

---

## 1. Procedimientos revisados

| Código | Nombre | Versión | Fecha | Realizado por |
|--------|--------|---------|-------|---------------|
| PR-ALM-001 | Recepción de mercancía | 3 | 20/04/2026 | Ing. Carlos Urbina |
| PR-ALM-002 | Ingreso al almacén | 3 | 16/04/2026 | Ing. Carlos Urbina |

---

## 2. Hipótesis del flujo principal (AS-IS)

```text
Logística notifica arribo
        ↓
Jefe de Almacén prepara recepción
        ↓
Auxiliar de Almacén verifica documentos
        ↓
Auxiliar de Almacén inspecciona físicamente
        ↓
¿Desfase / discrepancia?
   SÍ → Detener, FO-ALM-013, fotos, avisar Jefe → Jefe avisa Logística/VyF → esperar decisión
   NO → Llenar FO-ALM-003, etiquetas temporales, ubicar en zona temporal, preparar reporte de ingreso
        ↓
Ingreso formal al almacén (PR-ALM-002)
        ↓
Asignación de ubicación (Jefe de Almacén)
        ↓
Traslado y colocación (Auxiliar)
        ↓
Registro en SAE / Excel
        ↓
Etiquetado de ubicación
```

---

## 3. Puntos de inicio detectados (ambigüedad)

PR-ALM-001 presenta al menos dos puntos de inicio:

1. **Recepción de mercancía de proveedor** (4.1): inicia Logística al recibir confirmación del proveedor.
2. **Recepción de devoluciones de préstamo/consignación** (4.8): inicia el vendedor/cliente a través de Ventas y Facturación, sin intervención de Logística.

**Pregunta para la KES:** ¿La KES-Pilot modela solo el flujo de proveedor, o también el de devoluciones de préstamo? Si ambos, ¿son dos procesos distintos o variantes del mismo?

---

## 4. Vacíos y contradicciones detectados en la lectura

### 4.1 Responsable del registro en SAE

- PR-ALM-002 3.2 dice que el **Auxiliar de Almacén** "Registra en sistema todos los datos del ingreso".
- PR-ALM-002 4.4 dice que **Logística** "registrará obligatoriamente: número de entrada de almacén, código de producto y descripción, cantidad ingresada y unidad de medida en el SAE".
- PR-ALM-002 4.4 dice que el **Jefe de Almacén** "registrará: La ubicación exacta, lote y fecha de caducidad".

**Pregunta:** ¿Quién hace qué registro en el SAE? ¿Hay perfiles/permisos diferentes? ¿Se registran en la misma pantalla o en transacciones distintas?

### 4.2 Documentación previa vs. documentación al arribo

- PR-ALM-001 4.1 dice que Logística adjunta en la notificación: **orden de compra y factura**.
- PR-ALM-001 4.3 dice que el Auxiliar debe solicitar y revisar al momento de la llegada del transporte: factura, nota de remisión/carta porte, orden de compra, certificados.

**Pregunta:** ¿Logística envía copia digital antes y el Auxiliar recoge/vuelve a verificar el original físico al arribo? ¿O son documentos diferentes?

### 4.3 Registro de devoluciones de préstamo

- PR-ALM-001 4.8.2 dice "Grabar un video de la recepción de mercancía, adjuntándolo a un correo para respaldo, con copia a ventas y facturación, y gerencia".
- PR-ALM-001 4.8.3 dice cerrar el **vale de salida original (FO-ALM-012)**.
- No se tiene acceso al PR-ALM-006 (Entrega y Envío) ni al FO-ALM-012.

**Pregunta:** ¿El video es obligatorio solo para devoluciones de préstamo o también para recepciones normales? ¿Dónde se almacenan esos videos?

### 4.4 Control de entradas en Excel vs. SAE

- PR-ALM-001 5 lista "Registro en Excel: Control de entradas de almacén".
- PR-ALM-002 4.4 y 9 mencionan SAE / Excel/ERP.

**Pregunta:** ¿Se registra en Excel y en SAE? ¿Excel es respaldo, SAE es oficial? ¿O hay duplicidad?

### 4.5 Tiempo máximo documental vs. KPI general

- 4.7 dice "Recepción documental: Máximo 15 minutos".
- KPI dice "Tiempo promedio de recepción: Meta: <= 2 horas desde arribo hasta registro".

**Pregunta:** ¿El KPI de 2 horas incluye recepción documental, inspección física y registro? ¿Desde qué evento exacto se mide (arribo del transporte, notificación, inicio de descarga)?

### 4.6 Discrepancia y autorización

- 4.5 dice "NINGUNA mercancía con discrepancia puede continuar al ingreso sin autorización escrita del Jefe de Almacén y Logística".
- 4.6 habla de "Registro de Recepción Conforme" para mercancía que cumple.

**Pregunta:** ¿La autorización escrita es un correo, una nota en FO-ALM-013, una firma física? ¿Quién tiene la última palabra si Jefe de Almacén y Logística discrepan?

---

## 5. Términos y abreviaturas a validar

| Término/abreviatura | Uso detectado | Duda |
|---------------------|---------------|------|
| VyF | Ventas y Facturación | ¿Es el nombre oficial usado internamente? |
| SAE | Sistema de administración empresarial | ¿Es Aspel-SAE? ¿Versión? |
| FO-ALM-003 | Check list Recepción | ¿Es físico o digital? |
| FO-ALM-013 | Reporte de No Conformidad | ¿Se levanta por desfase, daño o ambos? |
| FO-ALM-012 | Vale de salida original | No disponible para revisión |
| PR-ALM-006 | Entrega y Envío | Referenciado pero no disponible |
| Trahiler | Tipo de transporte | ¿Es "tráiler" o una marca/tipo específico? |
| Patín | Equipo de carga | ¿Patin hidráulico? |
| Zona temporal | Área física | ¿Es la misma zona de recepción? |

---

## 6. Reglas críticas candidatas (pendientes de validar)

| ID temporal | Enunciado | Fuente | Pregunta de validación |
|-------------|-----------|--------|------------------------|
| R-ALM-PILOT-01 | La mercancía con discrepancia no continúa al ingreso sin autorización escrita del Jefe de Almacén y Logística. | PR-ALM-001 4.5 | ¿Qué forma toma la autorización? |
| R-ALM-PILOT-02 | Logística debe notificar el arribo con al menos 24 h de anticipación, o de inmediato si es urgente. | PR-ALM-001 4.1 | ¿Cómo se mide el cumplimiento? |
| R-ALM-PILOT-03 | La recepción documental debe completarse en máximo 15 minutos. | PR-ALM-001 4.7 | ¿Es una meta o un límite duro? |
| R-ALM-PILOT-04 | El ingreso solo procede si la mercancía fue previamente recepcionada y conforme. | PR-ALM-002 4.1, 6 | ¿Existe alguna excepción? |
| R-ALM-PILOT-05 | No se almacenan materiales incompatibles juntos. | PR-ALM-002 4.2 | ¿Dónde está la matriz de incompatibilidad? |

---

## 7. Decisiones clave a modelar

| Decisión | Opciones detectadas | Responsable declarado | Duda |
|----------|---------------------|-----------------------|------|
| ¿Aceptar, rechazar o retener mercancía con discrepancia? | Aceptar con nota / Rechazar / Solicitar reposición / Retener en zona de recepción | Logística da instrucciones; Jefe de Almacén aprueba/rechaza | ¿Quién decide finalmente? |
| ¿Asignar ubicación de almacenamiento? | Pasillo-rack-nivel-posición | Jefe de Almacén | ¿Hay reglas automáticas o siempre manual? |
| ¿Cerrar vale de salida por devolución? | Sí / No (si hay no conformidad) | Jefe de Almacén | ¿Quién autoriza si el material no está en condiciones? |

---

## 8. Eventos candidatos

| Evento | Generador | Disparador | Consumidor | Duda |
|--------|-----------|------------|------------|------|
| `ArriboNotificado` | Logística | Confirmación de proveedor | Almacén, VyF | ¿Siempre correo o también WhatsApp/llamada? |
| `TransporteLlego` | Auxiliar de Almacén | Llegada física | Jefe de Almacén | ¿Se registra hora de llegada? |
| `DocumentacionVerificada` | Auxiliar de Almacén | Revisión documental completa | Sistema/FO-ALM-003 | ¿Qué pasa si falta documento? |
| `InspeccionFisicaCompletada` | Auxiliar de Almacén | Fin de conteo/inspección | Jefe de Almacén | ¿Todos los productos se abren o solo muestras? |
| `DesfaseDetectado` | Auxiliar de Almacén | Discrepancia encontrada | Jefe de Almacén, Logística, VyF | ¿Se genera automáticamente FO-ALM-013? |
| `RecepcionConforme` | Auxiliar de Almacén | Sin discrepancias | PR-ALM-002 | ¿Evento único o por línea de producto? |
| `IngresoRegistradoEnSAE` | Logística / Auxiliar / Jefe | Finalización del registro | Inventario | ¿Quién lo genera? |
| `UbicacionAsignada` | Jefe de Almacén | Decisión de ubicación | Auxiliar de Almacén | ¿Se imprime etiqueta antes o después? |
| `ValeDeSalidaCerrado` | Jefe de Almacén | Devolución de préstamo conforme | VyF | ¿Notificación manual o automática? |

---

## 9. Objetos y atributos candidatos

| Objeto | Atributos detectados | Relaciones detectadas |
|--------|----------------------|-----------------------|
| Orden de compra | Número, proveedor, productos, cantidades | Dispara recepción |
| Factura del proveedor | Folio, fecha, datos fiscales, descripción | Se compara contra OC |
| Nota de remisión / Carta porte | Folio, transportista, origen, destino | Ampara transporte |
| Certificado de calidad | Número, laboratorio, fecha, resultado | Requerido según producto |
| Mercancía | Código, descripción, cantidad, lote, caducidad, empaque | Recibida, inspeccionada, ubicada |
| Checklist de recepción (FO-ALM-003) | Folio, fecha, resultado, firma | Evidencia de recepción conforme |
| Reporte de no conformidad (FO-ALM-013) | Folio, tipo de discrepancia, fotos, decisión | Detiene/condiciona ingreso |
| Vale de salida (FO-ALM-012) | Número, material, fecha salida, fecha devolución | Cierra devolución de préstamo |
| Ubicación | Almacén-pasillo-rack-nivel-posición | Se asigna a mercancía |
| Etiqueta de ubicación | Código de barras, producto, cantidad | Se imprime y coloca |
| Entrada de almacén (SAE/Excel) | Número, producto, cantidad, unidad, ubicación, lote | Registro oficial de inventario |

---

## 10. Known Unknowns ya detectados antes de la sesión

| ID | Pregunta | Prioridad | Vía de cierre |
|----|----------|-----------|---------------|
| KU-ALM-PILOT-01 | ¿El proceso de devoluciones de préstamo es parte de "Entrada de mercancía de proveedor" o es un proceso separado? | Alta | Definir alcance con Carlos/experto en KES-Pilot |
| KU-ALM-PILOT-02 | ¿Quién registra qué datos en el SAE durante el ingreso (Logística, Auxiliar o Jefe)? | Alta | Preguntar paso a paso en sesión |
| KU-ALM-PILOT-03 | ¿Existe duplicidad entre Excel y SAE? ¿Cuál es el sistema oficial de registro? | Alta | Preguntar en sesión |
| KU-ALM-PILOT-04 | ¿Dónde se almacenan las fotos y videos de evidencia? ¿Por cuánto tiempo? | Media | Preguntar en sesión |
| KU-ALM-PILOT-05 | ¿Cómo se mide el KPI "tiempo promedio de recepción <= 2 horas"? ¿Desde qué evento? | Media | Preguntar en sesión |
| KU-ALM-PILOT-06 | ¿Qué versión de SAE se usa (Aspel-SAE, otro ERP)? | Media | Preguntar en sesión |
| KU-ALM-PILOT-07 | ¿Hay una matriz de incompatibilidad de productos para asignar ubicaciones? | Media | Preguntar en sesión |
| KU-ALM-PILOT-08 | ¿Cuál es el flujo real cuando falta documentación al arribo? | Alta | Preguntar en sesión |

---

## 11. Assumptions de la prelectura

| ID | Suposición | Impacto si es falsa | Vía de validación |
|----|------------|---------------------|-------------------|
| AS-ALM-PILOT-01 | La KES-Pilot se centrará solo en el flujo de proveedor, no en devoluciones de préstamo. | Si es falsa, hay que incluir un segundo punto de inicio y más actores. | Confirmar alcance al inicio de la sesión. |
| AS-ALM-PILOT-02 | El SAE es Aspel-SAE y es el sistema oficial de inventario. | Si es falsa, el modelo de datos cambia. | Preguntar explícitamente. |
| AS-ALM-PILOT-03 | El Auxiliar de Almacén realiza la inspección física completa, no un inspector de calidad separado. | Si es falsa, hay un actor Calidad que falta. | Preguntar en sesión. |
| AS-ALM-PILOT-04 | "Patín" significa patín hidráulico. | Solo afecta nomenclatura. | Preguntar en sesión. |

---

## 12. Notas para el moderador (Kimi/CJ_OS)

- **No crear documentos maestros ni cambiar ontología/arquitectura/gobernanza** durante la sesión. Solo capturar en estas notas temporales.
- Empezar la sesión confirmando alcance: ¿solo proveedor o también devoluciones de préstamo?
- Pedir al experto que narre un caso real reciente (storytelling) antes de revisar el procedimiento línea por línea.
- Registrar cada hecho con fuente y evidencia. Si el experto dice algo que no está en el procedimiento, marcarlo como **hecho tácito**.
- Cuando aparezca una contradicción entre el procedimiento y la práctica real, registrarla como **excepción** o **Known Unknown**.
- Tomar nota de formatos físicos vs. digitales, ya que afecta el modelo de evidencia.
- Preguntar por el **peor día** posible en recepción: qué falla, quién decide, cómo se escala.

---

> **Nota:** Estas son notas temporales. El conocimiento validado se consolidará posteriormente en los documentos maestros correspondientes, una vez aprobado por Carlos.
