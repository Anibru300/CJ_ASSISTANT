# Plan de Rollback - Milestone M1 (Infraestructura)

> Fase M1.0 - Pre-Instalación  
> Propósito: describir exactamente cómo revertir el equipo al estado anterior si la instalación de Docker Desktop o los contenedores falla.

---

## 1. Alcance del rollback

Este plan aplica a los cambios que se realizarán durante el Milestone M1:

- Instalación de Docker Desktop.
- Habilitación de WSL2 y/o Hyper-V (si el instalador lo requiere).
- Descarga de imágenes Docker (n8n, PostgreSQL, Redis).
- Creación de contenedores y volúmenes.
- Modificación del PATH del sistema por Docker Desktop.

**No se modificarán archivos del proyecto CJ_Assistant durante M1**, por lo que no es necesario restaurar contenido del proyecto desde una copia externa.

---

## 2. Cómo desinstalar Docker Desktop

### Opción A - Desde Configuración de Windows (recomendada)

1. Abrir **Configuración** → **Aplicaciones** → **Aplicaciones instaladas**.
2. Buscar **Docker Desktop**.
3. Seleccionar **Desinstalar**.
4. Confirmar la desinstalación.
5. Reiniciar el equipo si se solicita.

### Opción B - Desde Panel de control

1. Abrir **Panel de control** → **Programas** → **Programas y características**.
2. Buscar **Docker Desktop**.
3. Clic derecho → **Desinstalar**.
4. Seguir el asistente y reiniciar si es necesario.

### Limpieza residual de Docker Desktop

Después de desinstalar, eliminar manualmente las carpetas residuales:

```powershell
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\Docker"
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\Docker Desktop"
Remove-Item -Recurse -Force "$env:PROGRAMDATA\Docker"
Remove-Item -Recurse -Force "$env:USERPROFILE\.docker"
```

> **Precaución:** ejecutar solo si se confirma que no hay datos importantes en esas rutas.

---

## 3. Cómo eliminar imágenes Docker

### Eliminar todas las imágenes

```bash
docker rmi -f $(docker images -q)
```

En PowerShell:

```powershell
docker images -q | ForEach-Object { docker rmi -f $_ }
```

### Eliminar imágenes específicas

```bash
docker rmi -f n8nio/n8n:latest
 docker rmi -f postgres:latest
 docker rmi -f redis:latest
```

---

## 4. Cómo eliminar contenedores

### Eliminar todos los contenedores (incluyendo los detenidos)

```bash
docker rm -f $(docker ps -aq)
```

En PowerShell:

```powershell
docker ps -aq | ForEach-Object { docker rm -f $_ }
```

### Eliminar contenedores del proyecto CJ_Assistant

```bash
cd "C:\Projects\CJ_Assistant\infrastructure\compose"
docker compose down
```

---

## 5. Cómo eliminar volúmenes

### Eliminar todos los volúmenes no utilizados

```bash
docker volume prune -f
```

### Eliminar volúmenes específicos del proyecto

```bash
cd "C:\Projects\CJ_Assistant\infrastructure\compose"
docker compose down -v
```

### Listar volúmenes antes de eliminar

```bash
docker volume ls
```

---

## 6. Cómo deshabilitar WSL2 (solo si fue habilitado durante la instalación)

### Desinstalar distribuciones de WSL

```powershell
wsl --unregister Ubuntu
```

> Reemplazar `Ubuntu` por el nombre de la distribución si es diferente.

### Deshabilitar la característica de WSL

```powershell
dism.exe /online /disable-feature /featurename:Microsoft-Windows-Subsystem-Linux
```

### Deshabilitar la plataforma de máquina virtual (requerida por WSL2)

```powershell
dism.exe /online /disable-feature /featurename:VirtualMachinePlatform
```

> **Nota:** Estos cambios requieren reinicio. Solo ejecutar si se decide revertir completamente WSL2.

---

## 7. Cómo deshabilitar Hyper-V (solo si fue habilitado durante la instalación)

```powershell
Disable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-All
```

Reiniciar el equipo si se solicita.

---

## 8. Cómo restaurar el proyecto CJ_Assistant

Durante M1 **no se modificarán** archivos dentro de:

```text
C:\Projects\CJ_Assistant\
```

Por lo tanto, el proyecto debería permanecer intacto. Para verificarlo:

```powershell
Test-Path "C:\Projects\CJ_Assistant\README.md"
Test-Path "C:\Projects\CJ_Assistant\docs"
```

Si por alguna razón se detectara algún cambio no deseado, se deberá recuperar desde la copia de seguridad más reciente disponible.

---

## 9. Verificación post-rollback

Después de ejecutar el rollback, confirmar:

1. Docker Desktop ya no aparece en la lista de aplicaciones instaladas.
2. No quedan contenedores: `docker ps -a` debe devolver lista vacía.
3. No quedan imágenes relevantes: `docker images` debe mostrar lista vacía o solo las de base.
4. No quedan volúmenes del proyecto: `docker volume ls` no muestra volúmenes de n8n/PostgreSQL/Redis.
5. El disco C: recupera el espacio consumido por Docker.
6. CJ_Assistant sigue estando en `C:\Projects\CJ_Assistant\`.

---

## 10. Responsable del rollback

- **Ingeniero DevOps (Kimi):** ejecutar el rollback siguiendo este plan.
- **Carlos (Product Owner):** autorizar el rollback si la instalación falla.

---

## 11. Cuándo activar el rollback

Se debe activar si ocurre cualquiera de los siguientes escenarios:

- Docker Desktop no inicia después de la instalación.
- El equipo presenta lentitud extrema o inestabilidad.
- Falla la verificación de `docker run hello-world`.
- Los contenedores de n8n/PostgreSQL/Redis no levantan correctamente.
- Se detecta pérdida de acceso a aplicaciones críticas (SAE, Outlook, etc.).
