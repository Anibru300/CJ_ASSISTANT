#!/bin/bash
set -e

cd "$(dirname "$0")/../compose" || exit 1

echo "Levantando servicios de CJ_OS..."
docker compose up -d

echo "Servicios activos:"
docker compose ps
