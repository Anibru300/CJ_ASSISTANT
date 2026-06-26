# Variables de Entorno - CJ_OS

> Documento maestro de configuración.
> Principio: **Nada de rutas absolutas ni credenciales dentro del código.**
> Todo se configura mediante el archivo `.env` ubicado en la raíz de `CJ_Assistant`.

---

## Ubicación del archivo de configuración

```text
CJ_Assistant/
└── .env
```

> **Nota de seguridad:** El archivo `.env` contiene contraseñas y rutas sensibles. No debe compartirse ni sincronizarse a repositorios públicos.

---

## 1. Configuración general del proyecto

| Variable | Descripción | Ejemplo | Requerido |
|----------|-------------|---------|-----------|
| `PROJECT_NAME` | Nombre del proyecto | `CJ_Assistant` | Sí |
| `PROJECT_VERSION` | Versión actual del proyecto | `0.0.6` | Sí |
| `TIMEZONE` | Zona horaria para logs y procesos | `America/Mexico_City` | Sí |
| `LOG_LEVEL` | Nivel de logging general | `info` | Sí |
| `ENVIRONMENT` | Entorno de ejecución | `development` / `production` / `testing` | Sí |

---

## 2. Rutas base del sistema

| Variable | Descripción | Ejemplo | Requerido |
|----------|-------------|---------|-----------|
| `WORKSPACE_ROOT` | Raíz del workspace persistente (archivos) | `./workspace` | Sí |
| `DOCS_PATH` | Carpeta de documentación | `./docs` | Sí |
| `CONFIG_PATH` | Carpeta de configuración por ambiente | `./config` | Sí |
| `CORE_PATH` | Carpeta del núcleo del sistema | `./core` | Sí |
| `AI_PATH` | Carpeta de la capa de IA | `./ai` | Sí |
| `CONNECTORS_PATH` | Carpeta de conectores externos | `./connectors` | Sí |
| `MODULES_PATH` | Carpeta de módulos de negocio | `./modules` | Sí |
| `PROMPTS_PATH` | Carpeta de prompts globales | `./prompts` | Sí |
| `TESTING_PATH` | Carpeta de pruebas y validaciones | `./testing` | Sí |
| `RUNTIME_PATH` | Carpeta de datos operativos (logs, caché, DBs) | `./runtime` | Sí |

---

## 3. Configuración de Docker

| Variable | Descripción | Ejemplo | Requerido |
|----------|-------------|---------|-----------|
| `COMPOSE_FILE` | Ruta al archivo compose principal | `./infrastructure/compose/docker-compose.yml` | Sí |
| `COMPOSE_PROJECT_NAME` | Nombre del proyecto en Docker | `cj_assistant` | Sí |
| `DOCKER_NETWORK_NAME` | Nombre de la red interna de Docker | `cj_network` | Sí |
| `DOCKER_SUBNET` | Subred interna de Docker | `172.20.0.0/16` | No |

---

## 4. Configuración de n8n

| Variable | Descripción | Ejemplo | Requerido |
|----------|-------------|---------|-----------|
| `N8N_PORT` | Puerto externo de n8n | `5678` | Sí |
| `N8N_HOST` | Host de n8n | `localhost` | Sí |
| `N8N_PROTOCOL` | Protocolo de n8n | `http` | Sí |
| `N8N_BASIC_AUTH_ACTIVE` | Activar autenticación básica | `true` | Sí |
| `N8N_BASIC_AUTH_USER` | Usuario de n8n | `admin` | Sí |
| `N8N_BASIC_AUTH_PASSWORD` | Contraseña de n8n | `cambiar_en_produccion` | Sí |
| `N8N_ENCRYPTION_KEY` | Clave de encriptación de credenciales | `clave-segura-32-caracteres` | Sí |
| `N8N_DATA_PATH` | Ruta de datos persistentes de n8n | `./runtime/n8n` | Sí |
| `WEBHOOK_URL` | URL base para webhooks | `http://localhost:5678/` | Sí |

---

## 5. Configuración de PostgreSQL

| Variable | Descripción | Ejemplo | Requerido |
|----------|-------------|---------|-----------|
| `POSTGRES_HOST` | Host de PostgreSQL | `postgres` | Sí |
| `POSTGRES_PORT` | Puerto externo de PostgreSQL | `5432` | Sí |
| `POSTGRES_DB` | Nombre de la base de datos | `cj_assistant` | Sí |
| `POSTGRES_USER` | Usuario de PostgreSQL | `cj_user` | Sí |
| `POSTGRES_PASSWORD` | Contraseña de PostgreSQL | `cambiar_en_produccion` | Sí |
| `POSTGRES_DATA_PATH` | Ruta de datos persistentes de PostgreSQL | `./runtime/database/postgres` | Sí |

---

## 6. Configuración de Redis

| Variable | Descripción | Ejemplo | Requerido |
|----------|-------------|---------|-----------|
| `REDIS_HOST` | Host de Redis | `redis` | Sí |
| `REDIS_PORT` | Puerto externo de Redis | `6379` | Sí |
| `REDIS_PASSWORD` | Contraseña de Redis | `cambiar_en_produccion` | Sí |
| `REDIS_DATA_PATH` | Ruta de datos persistentes de Redis | `./runtime/database/redis` | Sí |

---

## 7. Configuración de Inteligencia Artificial

| Variable | Descripción | Ejemplo | Requerido |
|----------|-------------|---------|-----------|
| `IA_PROVIDER` | Proveedor de IA a utilizar | `Kimi` | Sí |
| `IA_PROVIDER_API_KEY` | API Key del proveedor de IA | `token-seguro` | Sí |
| `IA_PROVIDER_MODEL` | Modelo específico del proveedor | `kimi-latest` | Sí |
| `IA_PROVIDER_ENDPOINT` | Endpoint base de la API (si aplica) | `https://api.moonshot.cn` | No |
| `IA_TIMEOUT_SECONDS` | Tiempo máximo de espera por respuesta | `60` | Sí |
| `IA_MAX_TOKENS` | Límite de tokens por solicitud | `4096` | No |
| `IA_TEMPERATURE` | Creatividad de las respuestas (0.0 - 1.0) | `0.3` | No |

---

## 8. Integraciones externas

### 8.1 OneDrive

| Variable | Descripción | Ejemplo | Requerido |
|----------|-------------|---------|-----------|
| `ONEDRIVE_PATH` | Ruta local sincronizada de OneDrive | `C:/Users/Usuario/OneDrive - Empresa` | Sí |
| `ONEDRIVE_PROJECT_FOLDER` | Carpeta del proyecto dentro de OneDrive | `CJ_Assistant` | Sí |

### 8.2 Google Drive

| Variable | Descripción | Ejemplo | Requerido |
|----------|-------------|---------|-----------|
| `GOOGLE_DRIVE_FOLDER` | ID o nombre de la carpeta de Google Drive | `CJ_Assistant_Drive` | Sí |
| `GOOGLE_SERVICE_ACCOUNT_JSON` | Ruta al archivo de credenciales de servicio | `./connectors/google_drive/credentials.json` | Sí |

### 8.3 Outlook

| Variable | Descripción | Ejemplo | Requerido |
|----------|-------------|---------|-----------|
| `OUTLOOK_EMAIL` | Correo de Outlook conectado | `correo@empresa.com` | Sí |
| `OUTLOOK_CLIENT_ID` | Client ID de la app de Microsoft | `client-id` | Sí |
| `OUTLOOK_CLIENT_SECRET` | Client Secret de la app de Microsoft | `client-secret` | Sí |
| `OUTLOOK_TENANT_ID` | Tenant ID de Microsoft 365 | `tenant-id` | Sí |

### 8.4 WhatsApp

| Variable | Descripción | Ejemplo | Requerido |
|----------|-------------|---------|-----------|
| `WHATSAPP_INSTANCE` | Identificador de la instancia de WhatsApp | `cj_assistant_prod` | Sí |
| `WHATSAPP_API_URL` | URL de la API de WhatsApp | `http://localhost:3000` | Sí |
| `WHATSAPP_API_TOKEN` | Token de autenticación de la API | `token-seguro` | Sí |

### 8.5 SAE (Aspel)

| Variable | Descripción | Ejemplo | Requerido |
|----------|-------------|---------|-----------|
| `SAE_DATABASE` | Ruta o nombre de la base de datos de SAE | `C:/Program Files (x86)/Aspel/Aspel-SAE 9.0/Datos/SAE.fdb` | Sí |
| `SAE_FIREBIRD_HOST` | Host del servidor Firebird | `localhost` | Sí |
| `SAE_FIREBIRD_PORT` | Puerto de Firebird | `3050` | Sí |
| `SAE_FIREBIRD_USER` | Usuario de Firebird | `SYSDBA` | Sí |
| `SAE_FIREBIRD_PASSWORD` | Contraseña de Firebird | `masterkey` | Sí |

### 8.6 Excel de almacén

| Variable | Descripción | Ejemplo | Requerido |
|----------|-------------|---------|-----------|
| `EXCEL_DATABASE` | Ruta al archivo maestro de Excel | `./connectors/excel/almacen.xlsx` | Sí |
| `EXCEL_SHEET_NAME` | Nombre de la hoja principal | `Inventario` | Sí |

---

## 9. Configuración de módulos

| Variable | Descripción | Ejemplo | Requerido |
|----------|-------------|---------|-----------|
| `MODULES_ENABLED` | Lista de módulos activos separados por coma | `almacen,ventas,sgc` | Sí |
| `MODULE_ALMACEN_ENABLED` | Activar módulo de almacén | `true` | No |
| `MODULE_VENTAS_ENABLED` | Activar módulo de ventas | `true` | No |
| `MODULE_COMPRAS_ENABLED` | Activar módulo de compras | `false` | No |
| `MODULE_CALIDAD_ENABLED` | Activar módulo de calidad | `false` | No |
| `MODULE_SGC_ENABLED` | Activar módulo SGC | `true` | No |
| `MODULE_RRHH_ENABLED` | Activar módulo de RRHH | `false` | No |
| `MODULE_LOGISTICA_ENABLED` | Activar módulo de logística | `false` | No |
| `MODULE_GERENCIA_ENABLED` | Activar módulo de gerencia | `false` | No |

---

## 10. Configuración de agentes

| Variable | Descripción | Ejemplo | Requerido |
|----------|-------------|---------|-----------|
| `AGENT_ALMACEN_ENABLED` | Activar agente de almacén | `true` | No |
| `AGENT_ALMACEN_MODEL` | Modelo específico del agente de almacén | `kimi-latest` | No |
| `AGENT_VENTAS_ENABLED` | Activar agente de ventas | `false` | No |
| `AGENT_COMPRAS_ENABLED` | Activar agente de compras | `false` | No |
| `AGENT_CALIDAD_ENABLED` | Activar agente de calidad | `false` | No |
| `AGENT_SGC_ENABLED` | Activar agente SGC | `false` | No |
| `AGENT_RRHH_ENABLED` | Activar agente de RRHH | `false` | No |
| `AGENT_LOGISTICA_ENABLED` | Activar agente de logística | `false` | No |
| `AGENT_GERENCIA_ENABLED` | Activar agente de gerencia | `false` | No |

---

## 11. Logs y respaldos

| Variable | Descripción | Ejemplo | Requerido |
|----------|-------------|---------|-----------|
| `LOGS_PATH` | Ruta donde se almacenan los logs | `./runtime/logs` | Sí |
| `BACKUPS_PATH` | Ruta donde se almacenan los respaldos | `./runtime/backups` | Sí |
| `BACKUP_RETENTION_DAYS` | Días de retención de respaldos | `30` | Sí |
| `TEMP_PATH` | Ruta de archivos temporales | `./runtime/temp` | Sí |
| `CACHE_PATH` | Ruta de archivos de caché | `./runtime/cache` | Sí |

---

## 12. Seguridad

| Variable | Descripción | Ejemplo | Requerido |
|----------|-------------|---------|-----------|
| `JWT_SECRET` | Clave secreta para tokens JWT | `clave-jwt-segura-64-caracteres` | Sí |
| `API_KEY` | Clave de API general del proyecto | `api-key-segura` | Sí |

---

## Ejemplo mínimo de archivo `.env`

```env
# General
PROJECT_NAME=CJ_Assistant
PROJECT_VERSION=0.0.6
TIMEZONE=America/Mexico_City
LOG_LEVEL=info
ENVIRONMENT=development

# Paths
WORKSPACE_ROOT=./workspace
DOCS_PATH=./docs
CONFIG_PATH=./config
CORE_PATH=./core
AI_PATH=./ai
CONNECTORS_PATH=./connectors
MODULES_PATH=./modules
PROMPTS_PATH=./prompts
TESTING_PATH=./testing
RUNTIME_PATH=./runtime

# Docker
COMPOSE_FILE=./infrastructure/compose/docker-compose.yml
COMPOSE_PROJECT_NAME=cj_assistant
DOCKER_NETWORK_NAME=cj_network

# n8n
N8N_PORT=5678
N8N_HOST=localhost
N8N_PROTOCOL=http
N8N_BASIC_AUTH_ACTIVE=true
N8N_BASIC_AUTH_USER=admin
N8N_BASIC_AUTH_PASSWORD=cambiar_en_produccion
N8N_ENCRYPTION_KEY=cambiar_por_clave_segura_de_32_chars
N8N_DATA_PATH=./runtime/n8n
WEBHOOK_URL=http://localhost:5678/

# PostgreSQL
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
POSTGRES_DB=cj_assistant
POSTGRES_USER=cj_user
POSTGRES_PASSWORD=cambiar_en_produccion
POSTGRES_DATA_PATH=./runtime/database/postgres

# Redis
REDIS_HOST=redis
REDIS_PORT=6379
REDIS_PASSWORD=cambiar_en_produccion
REDIS_DATA_PATH=./runtime/database/redis

# Integraciones
ONEDRIVE_PATH=C:/Users/Usuario/OneDrive - Empresa
ONEDRIVE_PROJECT_FOLDER=CJ_Assistant
GOOGLE_DRIVE_FOLDER=CJ_Assistant_Drive
GOOGLE_SERVICE_ACCOUNT_JSON=./connectors/google_drive/credentials.json
OUTLOOK_EMAIL=correo@empresa.com
OUTLOOK_CLIENT_ID=client-id
OUTLOOK_CLIENT_SECRET=client-secret
OUTLOOK_TENANT_ID=tenant-id
WHATSAPP_INSTANCE=cj_assistant_prod
WHATSAPP_API_URL=http://localhost:3000
WHATSAPP_API_TOKEN=token-seguro
SAE_DATABASE=C:/Program Files (x86)/Aspel/Aspel-SAE 9.0/Datos/SAE.fdb
SAE_FIREBIRD_HOST=localhost
SAE_FIREBIRD_PORT=3050
SAE_FIREBIRD_USER=SYSDBA
SAE_FIREBIRD_PASSWORD=masterkey
EXCEL_DATABASE=./connectors/excel/almacen.xlsx
EXCEL_SHEET_NAME=Inventario

# Logs y backups
LOGS_PATH=./runtime/logs
BACKUPS_PATH=./runtime/backups
BACKUP_RETENTION_DAYS=30
TEMP_PATH=./runtime/temp
CACHE_PATH=./runtime/cache

# Seguridad
JWT_SECRET=cambiar_por_clave_jwt_segura_de_64_caracteres_minimo
API_KEY=cambiar_por_api_key_segura
```

---

## Notas para el equipo

- Todas las rutas deben usar **rutas relativas** respecto a la raíz de `CJ_Assistant`.
- En Windows, Docker y los contenedores interpretan las rutas relativas según el contexto del `docker-compose.yml`.
- Las contraseñas deben cambiarse antes de pasar a producción.
