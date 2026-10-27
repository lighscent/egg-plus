#!/bin/sh
set -e
REGISTRY="${REGISTRY:-ghcr.io/lighscent/egg-plus}"
cd "$(dirname "$0")"
for v in $(grep -o '[0-9][0-9]*' ../versions.json); do
  echo "== nodejs_$v =="
  docker buildx build --platform linux/amd64,linux/arm64 \
    --build-arg NODE_VERSION="$v" \
    -t "$REGISTRY:nodejs_$v" --push .
done
echo "OK. Remember to update docker_images in egg-nodejs.json with $REGISTRY"
