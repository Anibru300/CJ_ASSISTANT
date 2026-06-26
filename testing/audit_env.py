#!/usr/bin/env python3
"""
Auditoria de seguridad de .env para CJ_OS.

Objetivo:
    Verificar si el archivo .env contiene valores que parezcan reales
    (credenciales de produccion, tokens, claves largas) vs. placeholders.

No imprime valores de variables sensibles.
"""

import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENV_PATH = PROJECT_ROOT / ".env"
EXAMPLE_PATH = PROJECT_ROOT / ".env.example"

# Variables que tipicamente contienen secretos
SENSITIVE_KEYS = {
    "N8N_BASIC_AUTH_PASSWORD",
    "N8N_ENCRYPTION_KEY",
    "POSTGRES_PASSWORD",
    "REDIS_PASSWORD",
    "JWT_SECRET",
    "API_KEY",
    "OUTLOOK_CLIENT_SECRET",
    "WHATSAPP_API_TOKEN",
    "SAE_FIREBIRD_PASSWORD",
    "GOOGLE_SERVICE_ACCOUNT_JSON",
}

# Patrones que indican placeholders obvios
PLACEHOLDER_PATTERNS = [
    re.compile(r"^cambiar[_\-]", re.IGNORECASE),
    re.compile(r"^cambiar_en_produccion$", re.IGNORECASE),
    re.compile(r"^token[-_]seguro$", re.IGNORECASE),
    re.compile(r"^client[-_]id$", re.IGNORECASE),
    re.compile(r"^client[-_]secret$", re.IGNORECASE),
    re.compile(r"^tenant[-_]id$", re.IGNORECASE),
    re.compile(r"^masterkey$", re.IGNORECASE),
    re.compile(r"^correo@empresa\.com$", re.IGNORECASE),
    re.compile(r"^admin$", re.IGNORECASE),
    re.compile(r"^\./connectors/.+\.json$", re.IGNORECASE),  # rutas a archivos de credenciales
]

# Variables que deberian ser largas y aleatorias en produccion
HIGH_ENTROPY_KEYS = {
    "N8N_ENCRYPTION_KEY",
    "JWT_SECRET",
    "API_KEY",
}


def parse_env(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    if not path.exists():
        return values
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue
        key, _, value = line.partition("=")
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def looks_like_placeholder(value: str) -> bool:
    if not value:
        return True
    for pattern in PLACEHOLDER_PATTERNS:
        if pattern.match(value):
            return True
    return False


def looks_real(value: str) -> bool:
    """Heuristica simple: si no es placeholder y tiene cierta complejidad, parece real."""
    if looks_like_placeholder(value):
        return False
    # Si es muy corto, probablemente sea un placeholder simple
    if len(value) < 8:
        return False
    return True


def main() -> int:
    env = parse_env(ENV_PATH)
    example = parse_env(EXAMPLE_PATH)

    print("=" * 60)
    print("AUDITORIA DE SEGURIDAD: .env")
    print("=" * 60)
    print(f"Archivo auditado: {ENV_PATH}")
    print(f"Variables encontradas: {len(env)}")
    print()

    # Variables presentes en .env.example pero no en .env
    missing_in_env = set(example.keys()) - set(env.keys())
    if missing_in_env:
        print("[!] Variables definidas en .env.example pero AUSENTES en .env:")
        for key in sorted(missing_in_env):
            print(f"    - {key}")
        print()

    # Variables en .env no presentes en .env.example
    extra_in_env = set(env.keys()) - set(example.keys())
    if extra_in_env:
        print("[!] Variables presentes en .env pero NO documentadas en .env.example:")
        for key in sorted(extra_in_env):
            print(f"    - {key}")
        print()

    # Variables sensibles
    print("Variables sensibles detectadas:")
    real_secrets: list[str] = []
    placeholder_secrets: list[str] = []
    weak_secrets: list[str] = []

    for key in sorted(SENSITIVE_KEYS):
        if key not in env:
            print(f"    - {key}: NO DEFINIDA")
            continue
        value = env[key]
        if looks_real(value):
            real_secrets.append(key)
            print(f"    - {key}: PARECE REAL (longitud {len(value)})")
        else:
            placeholder_secrets.append(key)
            print(f"    - {key}: PLACEHOLDER / DEFAULT")

        if key in HIGH_ENTROPY_KEYS and not looks_like_placeholder(value) and len(value) < 32:
            weak_secrets.append(key)

    print()
    print("Resumen:")
    print(f"    - Secretos que parecen reales: {len(real_secrets)}")
    print(f"    - Secretos con placeholder/default: {len(placeholder_secrets)}")
    print(f"    - Secretos debiles (cortos): {len(weak_secrets)}")

    if weak_secrets:
        print()
        print("[!] Los siguientes secretos parecen debiles (muy cortos):")
        for key in weak_secrets:
            print(f"    - {key}")

    print()
    if real_secrets:
        print("[ALERTA] El archivo .env contiene valores que parecen credenciales reales.")
        print("         Verificar que no sean de produccion y que .gitignore proteja .env.")
        return 1
    else:
        print("[OK] No se detectaron credenciales que parezcan reales; todo parece ser de desarrollo/placeholder.")
        return 0


if __name__ == "__main__":
    sys.exit(main())
