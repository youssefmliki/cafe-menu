#!/usr/bin/env python3
"""Publish MENU_HAUT.pdf as Menu Bas from 17:00 to 00:00 (Africa/Tunis)."""

from __future__ import annotations

import hashlib
import shutil
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
HAUT_ORIGINAL = ROOT / "source" / "MENU_HAUT_ORIGINAL.pdf"
MENU_BAS = ROOT / "MENU_BAS.pdf"
TARGET = ROOT / "MENU_HAUT.pdf"
TZ = ZoneInfo("Africa/Tunis")
EVENING_START = 17 * 60
TEST_NIGHT = date(2026, 9, 27)
TEST_START = 1 * 60
TEST_END = 1 * 60 + 20


def is_evening(now: datetime | None = None) -> bool:
    current = now or datetime.now(TZ)
    if current.tzinfo is None:
        current = current.replace(tzinfo=TZ)
    else:
        current = current.astimezone(TZ)
    minutes = current.hour * 60 + current.minute
    if current.date() == TEST_NIGHT and TEST_START <= minutes < TEST_END:
        return True
    return minutes >= EVENING_START


def file_hash(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    evening = is_evening()
    source = MENU_BAS if evening else HAUT_ORIGINAL
    slot = "bas" if evening else "haut"
    now = datetime.now(TZ).strftime("%Y-%m-%d %H:%M")

    if not MENU_BAS.exists():
        raise SystemExit(f"Missing source file: {MENU_BAS}")
    if not HAUT_ORIGINAL.exists():
        raise SystemExit(f"Missing source file: {HAUT_ORIGINAL}")

    if TARGET.exists() and file_hash(TARGET) == file_hash(source):
        print(f"{now} Africa/Tunis — MENU_HAUT.pdf already {slot}")
        return 0

    shutil.copyfile(source, TARGET)
    print(f"{now} Africa/Tunis — MENU_HAUT.pdf <- {source.name} ({slot})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
