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

## Nota sobre importación automática del workflow

La API REST de n8n (`/rest/workflows`) requiere autenticación mediante **API key** (`N8N_API_KEY`) o sesión de usuario. La autenticación básica (`N8N_BASIC_AUTH`) protege la interfaz web, pero no es suficiente para la API REST en las versiones recientes.

Por lo tanto, el workflow debe importarse de una de estas formas:

1. **Manualmente por GUI:**
   - Abrir `http://localhost:5678`.
   - Menú **Workflows** > **Import from File**.
   - Seleccionar `infrastructure/n8n/workflows/hello_world.json`.

2. **Configurar API key (opcional para automatizar):**
   - Agregar `N8N_API_KEY` en `.env` y `docker-compose.yml`.
   - Reiniciar n8n.
   - Usar la API REST con el header `X-N8N-API-KEY`.

## Estado actual

- ✅ Servidor Core funciona.
- ✅ Pruebas unitarias pasan.
- ✅ Docker y n8n corren.
- 🔄 Importación del workflow en n8n pendiente (requiere GUI o API key).
