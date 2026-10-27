#!/bin/sh
# Build + push tes images Node.js maison (multi-arch amd64/arm64).
# Usage: REGISTRY=ghcr.io/lighscent/egg-plus ./build.sh
# Prerequis: docker buildx, `docker login ghcr.io`
set -e
REGISTRY="${REGISTRY:-ghcr.io/lighscent/egg-plus}"
cd "$(dirname "$0")"
for v in $(grep -o '[0-9][0-9]*' ../versions.json); do
  echo "== nodejs_$v =="
  docker buildx build --platform linux/amd64,linux/arm64 \
    --build-arg NODE_VERSION="$v" \
    -t "$REGISTRY:nodejs_$v" --push .
done
echo "OK. Pense a mettre a jour docker_images dans egg-nodejs.json avec $REGISTRY"
