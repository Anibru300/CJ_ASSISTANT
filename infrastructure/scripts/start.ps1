$ErrorActionPreference = "Stop"

$ProjectRoot = Resolve-Path "$PSScriptRoot\..\.."
Set-Location $ProjectRoot

Write-Host "Levantando servicios de CJ_OS..."
docker compose --project-directory $ProjectRoot -f infrastructure\compose\docker-compose.yml up -d

Write-Host "Servicios activos:"
docker compose --project-directory $ProjectRoot -f infrastructure\compose\docker-compose.yml ps
