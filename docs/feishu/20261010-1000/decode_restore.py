#!/usr/bin/env python3
"""Restore the exact completed backup ZIP from the two tracked text parts."""
from pathlib import Path
import base64, hashlib
ROOT = Path(__file__).resolve().parent
PARTS = [ROOT / "backup.zip.base64.part1.txt", ROOT / "backup.zip.base64.part2.txt"]
EXPECTED = "3198e7171180a863469a29af93fe1f7fcd25cdb1b5812cfa054682fea6097758"
encoded = "".join(p.read_text(encoding="ascii").strip() for p in PARTS)
data = base64.b64decode(encoded, validate=True)
if len(data) != 618548 or hashlib.sha256(data).hexdigest() != EXPECTED:
    raise SystemExit("Backup verification failed; no output was written")
output = ROOT / "course-1000-completed-navigation-ppt.zip"
output.write_bytes(data)
print(f"Verified and restored {output.name}: {len(data)} bytes, SHA256 {EXPECTED}")
