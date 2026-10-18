from pathlib import Path
import base64, hashlib
root = Path(__file__).resolve().parent
encoded = "".join((root / f"evidence.zip.base64.part{i}.txt").read_text().strip() for i in range(1, 2))
data = base64.b64decode(encoded, validate=True)
if len(data) != 240288 or hashlib.sha256(data).hexdigest() != "bb265cae6ed87373d50853fd4091a2ad42bbfb0a22cbed19eeefcc51340288e2":
    raise SystemExit("Verification failed; no output written")
(root / "course-20261010-0800-evidence.zip").write_bytes(data)
print("Verified and restored course-20261010-0800-evidence.zip: 240288 bytes; SHA256 bb265cae6ed87373d50853fd4091a2ad42bbfb0a22cbed19eeefcc51340288e2")
