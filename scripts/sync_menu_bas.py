#!/usr/bin/env python3
"""Publish MENU_BAS.pdf with day or evening prices (Africa/Tunis)."""

from __future__ import annotations

import hashlib
import shutil
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
JOUR = ROOT / "source" / "MENU_BAS_JOUR.pdf"
SOIR = ROOT / "MENU_HAUT.pdf"
TARGET = ROOT / "MENU_BAS.pdf"
TZ = ZoneInfo("Africa/Tunis")
EVENING_START = 17 * 60
EVENING_END = 23 * 60 + 58


def is_evening(now: datetime | None = None) -> bool:
    current = now or datetime.now(TZ)
    if current.tzinfo is None:
        current = current.replace(tzinfo=TZ)
    else:
        current = current.astimezone(TZ)
    minutes = current.hour * 60 + current.minute
    return EVENING_START <= minutes < EVENING_END


def file_hash(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    evening = is_evening()
    source = SOIR if evening else JOUR
    slot = "soir" if evening else "jour"
    now = datetime.now(TZ).strftime("%Y-%m-%d %H:%M")

    if not source.exists():
        raise SystemExit(f"Missing source file: {source}")

    if TARGET.exists() and file_hash(TARGET) == file_hash(source):
        print(f"{now} Africa/Tunis — already {slot}")
        return 0

    shutil.copyfile(source, TARGET)
    print(f"{now} Africa/Tunis — MENU_BAS.pdf <- {source.name} ({slot})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
