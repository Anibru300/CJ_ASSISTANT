$ErrorActionPreference = "Stop"

$ProjectRoot = Resolve-Path "$PSScriptRoot\..\.."
Set-Location $ProjectRoot

Write-Host "Deteniendo servicios de CJ_OS..."
docker compose --project-directory $ProjectRoot -f infrastructure\compose\docker-compose.yml down

Write-Host "Servicios detenidos."
