# Egg Node.js (images maison)

- Egg : `egg-nodejs.json` (format `PTDL_v2`)
- Images : `nodejs/image/Dockerfile` + `entrypoint.sh`, un seul Dockerfile pour les 5 versions via `NODE_VERSION`.

## 1. Builder et publier

```sh
cd nodejs/image
REGISTRY=ghcr.io/mon-org/eggs ./build.sh
```

Remplace ensuite `ghcr.io/CHANGE-ME/eggs` dans `egg-nodejs.json` par ton registre.

## 2. Importer dans Pterodactyl

Nests → Import Egg → colle `egg-nodejs.json`.
