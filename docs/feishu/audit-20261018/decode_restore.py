#!/usr/bin/env python3
"""Restore the read-only course audit snapshot without modifying remote documents."""
from pathlib import Path
import base64, hashlib
ROOT = Path(__file__).resolve().parent
PARTS = 2
EXPECTED_SHA256 = "6e2885a2512e7550e1e07ffc01b6961a684431a2ad564f0a8d6c1a9a79a608ca"
EXPECTED_SIZE = 598721
encoded = "".join((ROOT / f"backup.zip.base64.part{i}.txt").read_text(encoding="ascii").strip() for i in range(1, PARTS + 1))
data = base64.b64decode(encoded, validate=True)
if len(data) != EXPECTED_SIZE or hashlib.sha256(data).hexdigest() != EXPECTED_SHA256:
    raise SystemExit("Verification failed; no output written")
output = ROOT / "feishu-course-audit-20261018.zip"
output.write_bytes(data)
print(f"Verified and restored {output.name}: {len(data)} bytes; SHA256 {EXPECTED_SHA256}")
