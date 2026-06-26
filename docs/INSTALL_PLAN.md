# Plan de Instalación - Milestone M1 (Infraestructura)

> Fase M1.0 - Pre-Instalación  
> Estado: Documentación lista, en ejecución.

---

## 1. Objetivo de Docker

Proporcionar el entorno de ejecución de contenedores para CJ_OS. Docker Desktop permitirá ejecutar de forma aislada y reproducible los servicios de automatización, base de datos y caché, garantizando que el entorno de desarrollo sea idéntico en cualquier equipo.

## 2. Objetivo de n8n

n8n será el motor de automatización de flujos de trabajo (workflows). Se utilizará para conectar CJ_OS con WhatsApp, OneDrive, Outlook, Google Drive, SAE y Excel de almacén.

## 3. Objetivo de PostgreSQL

PostgreSQL será la base de datos transaccional principal del proyecto. Almacenará configuraciones, estados de workflows, registros de conversaciones, metadatos de integraciones y datos operativos.

> **Nota:** PostgreSQL se instalará como contenedor dentro de Docker, no de forma nativa.

## 4. Objetivo de Redis

Redis se utilizará como sistema de caché y broker de colas para tareas asíncronas. Ayudará a mejorar el rendimiento de n8n y a gestionar procesos en segundo plano.

> **Nota:** Redis se instalará como contenedor dentro de Docker, no de forma nativa.

---

## 5. Arquitectura prevista

```text
┌─────────────────────────────────────────┐
│           Windows 10 Pro                │
│                                         │
│  ┌─────────────────────────────────┐    │
│  │        Docker Desktop           │    │
│  │  ┌─────────┐ ┌─────────────┐   │    │
│  │  │   n8n   │ │  PostgreSQL │   │    │
│  │  └────┬────┘ └─────────────┘   │    │
│  │       │        ┌─────────┐     │    │
│  │       └────────┤  Redis  │     │    │
│  │                └─────────┘     │    │
│  └─────────────────────────────────┘    │
│                                         │
│  Conexiones externas:                   │
│  - WhatsApp                             │
│  - OneDrive                             │
│  - Outlook                              │
│  - Google Drive                         │
│  - SAE (Aspel)                          │
│  - Excel de almacén                     │
└─────────────────────────────────────────┘
```

---

## 6. Riesgos conocidos

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|-------------:|--------:|------------|
| Espacio insuficiente en disco C: (~26 GB libres) | Media | Alto | Limpieza previa realizada. Monitorear uso de imágenes Docker y limitar tamaño del disco virtual. |
| WSL2 requiere virtualización y puede fallar en equipos con BIOS antigua | Baja | Alto | Virtualización confirmada habilitada en BIOS. |
| Hyper-V/WSL2 pueden no estar habilitados en Windows 10 Pro | Media | Alto | El instalador de Docker Desktop puede habilitarlos automáticamente; de lo contrario, habilitarlos manualmente como administrador. |
| Rendimiento limitado por hardware (Intel i3-4150, 8 GB RAM) | Alta | Medio | Configurar límites de recursos en Docker Desktop: 2 CPUs, 4 GB RAM máximo, swap limitado. No ejecutar todos los contenedores en producción hasta actualizar hardware. |
| Conflicto con Kimi CLI u otras herramientas por puertos comunes | Baja | Medio | Usar puertos estándar documentados en `.env` y ajustar si hay colisiones. |
| Pérdida de datos de configuración si no se respalda | Baja | Alto | Datos persistentes fuera de Docker en `runtime/`. Proyecto respaldado en ubicación fija. |

---

## 7. Requisitos del sistema

### 7.1 Requisitos de software

| Componente | Requisito | Estado actual |
|------------|-----------|---------------|
| Sistema operativo | Windows 10 Pro/Enterprise/Education v1903+ o Windows 11 | ✅ Windows 10 Pro build 19045 |
| WSL2 | Requerido para Docker Desktop en Windows 10 | ⚠️ Pendiente de habilitar durante instalación |
| Hyper-V | Requerido o recomendado según backend | ⚠️ Pendiente de habilitar durante instalación |
| Virtualización en BIOS | Requerida | ✅ Habilitada |

### 7.2 Requisitos de hardware

| Componente | Mínimo recomendado | Estado actual |
|------------|-------------------:|---------------|
| Procesador | 64 bits con virtualización | ✅ Intel i3-4150 (2C/4T) |
| RAM | 8 GB mínimo | ✅ 8 GB |
| Disco libre | 20 GB mínimo para Docker + imágenes | ⚠️ ~26 GB libres (justo) |

### 7.3 Requisitos de red

| Requisito | Estado |
|-----------|--------|
| Conexión a Internet para descargar Docker Desktop | ✅ Disponible |
| Conexión a Internet para descargar imágenes oficiales de Docker Hub | ✅ Disponible |

---

## 8. Lista exacta de pasos de instalación

### Fase M1.1 - Preparación del sistema

1. Verificar que haya al menos 20 GB libres en disco C:.
2. Confirmar que la virtualización esté habilitada en BIOS.
3. Cerrar aplicaciones que consuman mucha RAM (Chrome, Outlook, etc.) para liberar recursos.
4. Crear un punto de restauración de Windows (opcional pero recomendado).

### Fase M1.2 - Reorganización física de carpetas

1. Crear la estructura de carpetas definitiva en `C:\Projects\CJ_Assistant\` según `ARCHITECTURE.md`.
2. Mover la documentación actual a `docs/`.
3. Crear carpetas vacías de `core/`, `ai/`, `connectors/`, `modules/`, `workspace/`, `runtime/`, `config/` y `testing/`.
4. Crear archivo `.env` con la configuración inicial de desarrollo.
5. Crear archivos base en `config/development/`.

### Fase M1.3 - Descarga de Docker Desktop

1. Descargar Docker Desktop para Windows desde el sitio oficial.
2. Guardar el instalador en `C:\temp\` o ubicación temporal.
3. Verificar la firma digital del instalador antes de ejecutarlo.

### Fase M1.4 - Instalación de Docker Desktop

1. Ejecutar el instalador de Docker Desktop como administrador.
2. Durante la instalación, seleccionar el backend de WSL2.
3. Esperar a que el instalador complete la instalación y reinicie si es necesario.
4. Una vez reiniciado, abrir Docker Desktop.
5. Aceptar los términos de servicio y completar la configuración inicial.
6. Verificar que Docker Desktop muestre "Engine running".

### Fase M1.5 - Verificación de Docker

1. Abrir una terminal nueva (cmd, PowerShell o Git Bash).
2. Ejecutar: `docker --version`
3. Ejecutar: `docker compose version`
4. Ejecutar: `docker run hello-world`
5. Confirmar que todos los comandos respondan correctamente.

### Fase M1.6 - Configuración de recursos de Docker

1. Abrir Docker Desktop → Settings → Resources.
2. Configurar límites según el hardware:
   - CPUs: 2
   - Memory: 4 GB (ajustar a 3 GB si el sistema opera con poca RAM)
   - Swap: 1 GB
   - Disk image size: 24 GB (máximo recomendado con ~26 GB libres)
3. Aplicar cambios y esperar reinicio de Docker Desktop.

### Fase M1.7 - Preparación de archivos de configuración

1. Crear `infrastructure/compose/docker-compose.yml`.
2. Definir servicios: n8n, PostgreSQL, Redis.
3. Configurar volúmenes persistentes apuntando a `runtime/` para no perder datos.
4. Usar variables de entorno del archivo `.env`.

### Fase M1.8 - Levantamiento inicial de servicios

1. Desde `C:\Projects\CJ_Assistant\infrastructure\compose\`, ejecutar: `docker compose up -d`
2. Verificar que los contenedores estén corriendo: `docker compose ps`
3. Acceder a n8n en `http://localhost:5678` para confirmar que funciona.
4. Detener los contenedores si no se van a usar inmediatamente: `docker compose down`

### Fase M1.9 - Documentación post-instalación

1. Registrar en `INSTALL_LOG.md` cada acción realizada con fecha, hora, versión y resultado.
2. Actualizar `CHANGELOG.md` con los avances de M1.
3. Actualizar `SYSTEM_MAP.md` con los componentes instalados.
4. Actualizar `TECH_STACK.md` con las versiones concretas.

---

## 9. Criterios de aceptación de M1

- Docker Desktop está instalado y ejecutándose.
- Los comandos `docker --version`, `docker compose version` y `docker run hello-world` funcionan.
- Los contenedores de n8n, PostgreSQL y Redis pueden levantarse con `docker compose up -d`.
- La interfaz web de n8n responde en `http://localhost:5678`.
- El plan de rollback está probado y documentado.
