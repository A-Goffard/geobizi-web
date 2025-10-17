#!/usr/bin/env bash
set -euo pipefail

if ! command -v wg >/dev/null 2>&1; then
  echo "wg no encontrado. Instala wireguard-tools (apt install wireguard-tools) o ejecuta en una máquina con wg."
  exit 1
fi

OUTDIR=${1:-.}
mkdir -p "$OUTDIR"

for NAME in server client1 client2; do
  echo "Generando claves para: $NAME"
  (wg genkey | tee "$OUTDIR/${NAME}_private.key" | wg pubkey > "$OUTDIR/${NAME}_public.key")
done

echo "Claves generadas en $OUTDIR. Ejemplos:"
ls -la "$OUTDIR"/*_private.key "$OUTDIR"/*_public.key || true
echo "Recuerda mover las private keys a un sitio seguro y no subirlas al repo."
