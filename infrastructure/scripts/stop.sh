#!/bin/bash
set -e

cd "$(dirname "$0")/../compose" || exit 1

echo "Deteniendo servicios de CJ_OS..."
docker compose down

echo "Servicios detenidos."
