# CJ_OS — Hello World end-to-end

**Versión:** 0.0.18  
**Propósito:** Validar que n8n puede comunicarse con el Core de CJ_OS antes de avanzar al Modelo de Datos.

---

## Arquitectura de la prueba

```text
[n8n] --HTTP GET--> [Core: core/api/hello_world.py] --JSON--> [n8n]
```

1. n8n dispara el workflow manualmente.
2. El nodo **HTTP Request** llama al endpoint `/hello` del Core.
3. El Core responde con un JSON.
4. n8n muestra la respuesta en el último nodo.

---

## Archivos creados

| Archivo | Propósito |
|---------|-----------|
| `core/api/hello_world.py` | Servidor HTTP minimalista del Core. Expone `/hello` (GET y POST). |
| `core/hello_world_cli.py` | Versión CLI del Hello World, invocable por n8n con `Execute Command`. |
| `testing/test_hello_world.py` | Pruebas básicas del CLI y del módulo HTTP. |
| `infrastructure/n8n/workflows/hello_world.json` | Workflow exportable para n8n. |

---

## Instrucciones de prueba

### 1. Iniciar el servidor del Core

Desde la raíz del proyecto:

```bash
cd /c/Projects/CJ_Assistant
python core/api/hello_world.py
```

Por defecto escucha en el puerto `8000`. Para cambiarlo:

```bash
HELLO_WORLD_PORT=8080 python core/api/hello_world.py
```

### 2. Probar localmente

```bash
curl http://localhost:8000/hello
```

Respuesta esperada:

```json
{
  "status": "ok",
  "message": "Hola desde el Core de CJ_OS",
  "version": "0.0.18",
  "component": "core/api/hello_world.py"
}
```

También soporta POST:

```bash
curl -X POST http://localhost:8000/hello \
  -H "Content-Type: application/json" \
  -d '{"name": "Francisco"}'
```

### 3. Importar el workflow en n8n

1. Abrir n8n en `http://localhost:5678`.
2. Menú **Workflows** > **Import from File**.
3. Seleccionar `infrastructure/n8n/workflows/hello_world.json`.
4. Guardar y hacer clic en **Test workflow**.

> Si n8n corre dentro de Docker y el Core fuera, usar `http://host.docker.internal:8000/hello`.
> Si n8n corre fuera de Docker, usar `http://localhost:8000/hello`.

### 4. Ejecutar las pruebas automáticas

```bash
python testing/test_hello_world.py
```

---

## Notas

- Este es el **primer código** de CJ_OS. No contiene lógica de negocio real.
- El servidor usa solo la librería estándar de Python (`http.server`). No requiere instalar dependencias.
- La API no es pública ni definitiva; es una prueba de arquitectura.

---

## Bloqueo actual

Para ejecutar el workflow end-to-end se requiere que **Docker Desktop esté activo** y n8n esté corriendo. En este momento Docker no está disponible, por lo que la prueba manual con curl y las pruebas unitarias del CLI sí funcionan, pero la integración con n8n queda pendiente de reinicio de Docker.
