#!/usr/bin/env python3
"""Sync nodejs/versions.json + egg docker_images avec le calendrier Node.js.

Politique : ajoute les majeures supportees manquantes
(start <= aujourd'hui <= end selon nodejs/Release schedule.json).
Ne supprime jamais les EOL (arbitrage manuel : des serveurs
peuvent encore referencer l'ancienne image).
"""
import json
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSIONS_FILE = ROOT / "versions.json"
EGG_FILE = ROOT / "egg-nodejs.json"
IMAGE_PREFIX = "ghcr.io/lighscent/egg-plus:nodejs_"
SCHEDULE_URL = "https://raw.githubusercontent.com/nodejs/Release/main/schedule.json"


def supported_majors(today: date) -> list[str]:
    with urllib.request.urlopen(SCHEDULE_URL) as r:
        schedule = json.load(r)
    majors = []
    for key, info in schedule.items():
        major = key.lstrip("v")
        if not major.isdigit() or not info.get("start") or not info.get("end"):
            continue
        if date.fromisoformat(info["start"]) <= today <= date.fromisoformat(info["end"]):
            majors.append(major)
    return sorted(majors, key=int)


def main() -> None:
    today = date.today()
    supported = supported_majors(today)
    versions = json.loads(VERSIONS_FILE.read_text())
    missing = [m for m in supported if m not in versions]
    if not missing:
        print(f"OK, a jour au {today} : {versions}")
        return

    versions = sorted(set(versions) | set(missing), key=int)
    VERSIONS_FILE.write_text(json.dumps(versions, indent=2) + "\n")
    print(f"versions ajoutees : {missing}")

    egg = json.loads(EGG_FILE.read_text())
    for major in missing:
        egg["docker_images"][f"Nodejs {major}"] = f"{IMAGE_PREFIX}{major}"
    egg["docker_images"] = dict(
        sorted(egg["docker_images"].items(), key=lambda kv: int(kv[0].split()[-1]))
    )
    EGG_FILE.write_text(json.dumps(egg, indent=4, ensure_ascii=False) + "\n")
    print("egg-nodejs.json mis a jour")


if __name__ == "__main__":
    main()
