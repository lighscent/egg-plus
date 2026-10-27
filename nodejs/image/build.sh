#!/bin/sh
# Build + push tes images Node.js maison (multi-arch amd64/arm64).
# Usage: REGISTRY=ghcr.io/mon-org/eggs ./build.sh
# Prerequis: docker buildx, `docker login ghcr.io`
set -e
REGISTRY="${REGISTRY:-ghcr.io/CHANGE-ME/eggs}"
cd "$(dirname "$0")"
for v in 20 22 24 25 26; do
  echo "== nodejs_$v =="
  docker buildx build --platform linux/amd64,linux/arm64 \
    --build-arg NODE_VERSION="$v" \
    -t "$REGISTRY:nodejs_$v" --push .
done
echo "OK. Pense a mettre a jour docker_images dans egg-nodejs.json avec $REGISTRY"
