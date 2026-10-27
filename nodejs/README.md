# Egg Node.js (images maison)

- Egg : `egg-nodejs.json` (format `PTDL_v2`)
- Images : `nodejs/image/Dockerfile` + `entrypoint.sh`, un seul Dockerfile pour toutes les versions via `NODE_VERSION`.
- Versions : `nodejs/versions.json` = source unique (build local, CI, egg).

## Mises à jour auto (CVE)

- Patchs : tags majeurs flottants (`node:24-trixie-slim`) + rebuild hebdo GitHub (lundi 4h) → derniers patchs CVE sans rien faire.
- Majeures : `check-node-versions.yml` (1er du mois) compare au calendrier officiel Node.js et ouvre une PR si une majeure supportée manque. Les EOL ne sont jamais supprimées auto.

## 1. Builder et publier

```sh
cd nodejs/image
./build.sh
```

Le workflow GitHub (`.github/workflows/docker-nodejs.yml`) build et publie auto vers `ghcr.io/lighscent/egg-plus:nodejs_XX` à chaque push sur `nodejs/image/**`, chaque lundi 4h, ou en manuel.

## 2. Importer dans Pterodactyl

Nests → Import Egg → colle `egg-nodejs.json`.
