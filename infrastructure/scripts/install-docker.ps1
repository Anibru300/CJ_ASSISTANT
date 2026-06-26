#Requires -RunAsAdministrator

$ErrorActionPreference = "Stop"

$InstallerPath = "C:\temp\DockerDesktopInstaller.exe"
$ProjectRoot = Resolve-Path "$PSScriptRoot\..\.."

if (-not (Test-Path $InstallerPath)) {
    Write-Error "No se encontró el instalador en $InstallerPath. Descárgalo primero desde https://www.docker.com/products/docker-desktop/"
    exit 1
}

Write-Host "Creando punto de restauración..."
try {
    Checkpoint-Computer -Description "Antes de Docker Desktop CJ_OS" -RestorePointType "MODIFY_SETTINGS"
    Write-Host "Punto de restauración creado."
} catch {
    Write-Warning "No se pudo crear el punto de restauración: $_"
}

Write-Host "Instalando Docker Desktop con backend WSL2 en modo silencioso..."
Start-Process -FilePath $InstallerPath -ArgumentList "install", "--quiet", "--accept-license=rgba", "--backend=wsl-2" -Wait

Write-Host "Docker Desktop instalado. Reinicia el equipo si el instalador lo solicita."
Write-Host "Después del reinicio, configura recursos desde Docker Desktop: Settings > Resources:"
Write-Host "  - CPUs: 2"
Write-Host "  - Memory: 4 GB (o 3 GB si el sistema opera con poca RAM)"
Write-Host "  - Swap: 1 GB"
Write-Host "  - Disk image size: 24 GB"
