# Stack Tecnológico - CJ_OS

## Sistema Operativo

- Windows 10 Pro (build 19045), 64 bits
- WSL2 (pendiente de habilitar durante instalación de Docker Desktop)

## Hardware de desarrollo

- Procesador: Intel Core i3-4150 (2C/4T)
- RAM: 8 GB
- Disco: ~25 GB libres en C:

## Contenedores

- Docker Desktop (en instalación)
- Docker Compose v2 (incluido en Docker Desktop)

## Base de Datos

- PostgreSQL 16 (Alpine)
- Redis 7 (Alpine)

## Automatización

- n8n (imagen oficial `n8nio/n8n:latest`)

## Inteligencia Artificial

- Proveedor principal: Kimi (configurable vía `IA_PROVIDER`)
- Proveedores alternativos: OpenAI, Anthropic Claude, Google Gemini

## Lenguajes y herramientas de desarrollo

- Python 3.11.9
- Node.js v24.14.0
- npm 11.9.0
- Git 2.53.0
- VS Code 1.125.1

## ERP y sistemas externos

- Aspel SAE 9.0 (Firebird)
- Microsoft 365 (OneDrive, Outlook)
- Google Drive
- WhatsApp (API o puente)
- Microsoft Excel (inventario de almacén)

## Almacenamiento

- Archivos fuente de verdad: `workspace/`
- Datos operativos: `runtime/`
- Respaldos: `runtime/backups/`

## Versionado

- Git 2.53.0
- Esquema semántico provisional: 0.0.x
