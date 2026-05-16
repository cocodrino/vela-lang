#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VOICES_DIR="$ROOT_DIR/voices"

mkdir -p "$VOICES_DIR"

echo "[vela-tts-piper] Setup base completo (sin descarga automática)."
echo "1) Instala Piper en tu sistema y ubica el binario."
echo "2) Descarga modelo .onnx y .onnx.json en: $VOICES_DIR"
echo "3) Configura variables en tu entorno (.env recomendado):"
echo "   PIPER_BIN=/ruta/a/piper"
echo "   PIPER_MODEL=$VOICES_DIR/tu-voz.onnx"
echo "   PIPER_CONFIG=$VOICES_DIR/tu-voz.onnx.json"
echo "   PIPER_INPUT_MODE=text"
echo "   VELA_DICT_PATH=$ROOT_DIR/data/vela-dictionary.json"
echo "4) Ejecuta validación: npm run tts:doctor"
