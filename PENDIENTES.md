# Pendientes CJ_OS - Revisión del 26 de junio de 2026

> Reunión con: Carlos, Francisco y Kimi.  
> Se apagó la computadora antes de continuar. Retomar desde aquí.

---

## ✅ Lo que ya se hizo hoy

1. **Revisión general del proyecto CJ_OS**:
   - Se identificó que el proyecto está en fase M2 (diseño/documentación) con infraestructura base funcionando (Docker, PostgreSQL, Redis, n8n).
   - No hay código de aplicación aún en `ai/`, `connectors/`, `modules/`, `core/`, `testing/`.
   - Se detectaron riesgos críticos y se corrigieron los más urgentes.

2. **Archivos creados/corregidos**:
   - `.env.example`: plantilla segura con todas las variables de entorno.
   - `.gitignore`: protege secretos, datos locales (`runtime/`, `02_backups/`, `03_logs/`) y archivos de entorno.
   - `infrastructure/compose/docker-compose.yml`: se fijó la imagen de n8n a `n8nio/n8n:1.84.0` (antes estaba en `latest`).

3. **Limpieza de estructura**:
   - Se eliminaron las carpetas numeradas vacías (`01_n8n/`, `04_google_drive/`, `05_onedrive/`, `06_sae/`, `07_excel_almacen/`, `08_whatsapp/`, `09_prompts/`, `10_pruebas/`).
   - Motivo: duplicaban la estructura real (`ai/`, `connectors/`, `modules/`, `workspace/`, etc.) y generaban confusión.
   - La información sobre su propósito histórico queda en este archivo y en `docs/CHANGELOG.md`.

4. **Repositorio Git y GitHub**:
   - Se inicializó el repositorio local.
   - Se configuró el remoto `origin` apuntando a `https://github.com/Anibru300/CJ_ASSISTANT`.
   - Se realizó el commit inicial y se subió el proyecto.
   - Verificación: `.env`, `runtime/`, `02_backups/` y `03_logs/` quedan fuera del repositorio gracias a `.gitignore`.

---

## ⚠️ Pendiente de aplicar (IMPORTANTE)

### 1. Reiniciar n8n con la versión fija
El cambio de versión en `docker-compose.yml` **aún no se aplica** porque el contenedor sigue corriendo con la imagen anterior (`latest`) o Docker no está activo.

**Pasos al reanudar:**

```bash
cd /c/Projects/CJ_Assistant/infrastructure/compose
docker compose down
docker compose pull
docker compose up -d
```

> Antes de hacer `docker compose up -d`, verificar que la base de datos actual de n8n no provenga de una versión mayor a `1.84.0`. Si es mayor, hay que actualizar el `docker-compose.yml` a esa versión para evitar errores de migración.

### 2. Corregir inconsistencia en variables de IA
- `docs/ENVIRONMENT.md` menciona variables `IA_PROVIDER`, `IA_PROVIDER_API_KEY`, `IA_PROVIDER_MODEL`, etc., que **no están en `.env`**.
- El `.env` actual tiene `AGENT_ALMACEN_MODEL`, que **no aparece documentado** en `docs/ENVIRONMENT.md`.

**Decisión pendiente:** unificar el proveedor de IA central vs. modelo por agente. Requiere validación de Carlos.

### 3. Corregir inconsistencias documentales del reporte M2.4
Según el propio reporte M2.4, faltan correcciones en:
- Número de capas del Core (unificar a 5).
- Actualizar `SYSTEM_MAP.md`.
- Revisar `docs/archive/CORE_ARCHITECTURE.md`.

### 4. Crear un "Hello World" end-to-end
Validar que la arquitectura propuesta funciona:
- Workflow de n8n → invoca script Python del Core → devuelve respuesta.
- Esto confirmaría que n8n puede comunicarse con el futuro código del sistema.

### 5. Revisar espacio en disco
El disco C: está al ~94% con ~15 GB libres. Monitorear porque el crecimiento de n8n/PostgreSQL puede detener todo.

---

## ❓ Preguntas sin resolver

1. ¿El `.env` actual contiene credenciales de producción reales o solo de desarrollo?
2. ¿El hardware actual (i3, 8 GB RAM) será el entorno definitivo o hay plan de escalar?
3. ¿Cuándo se espera iniciar la fase de código (M3 / Modelo de Datos)?
4. ¿Se usará un proveedor de IA central (`IA_PROVIDER`) o modelo por agente (`AGENT_*_MODEL`)?

---

## 🛑 Recordatorio de apagado

Antes de apagar la computadora, si Docker está corriendo, detener los contenedores para evitar corrupción de datos:

```bash
cd /c/Projects/CJ_Assistant/infrastructure/compose
docker compose down
```

Si ya se apagó sin hacerlo, al reiniciar revisar que PostgreSQL y n8n levanten correctamente:

```bash
docker compose up -d
docker compose ps
```

---

*Última actualización: 2026-06-26 por Kimi (revisión con Carlos y Francisco).*
