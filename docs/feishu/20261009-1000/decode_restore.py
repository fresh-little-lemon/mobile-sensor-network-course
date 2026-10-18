from pathlib import Path
import base64, hashlib
root = Path(__file__).resolve().parent
encoded = "".join((root / f"evidence.zip.base64.part{i}.txt").read_text().strip() for i in range(1, 2))
data = base64.b64decode(encoded, validate=True)
if len(data) != 288608 or hashlib.sha256(data).hexdigest() != "a529fceef00b7fd4263b8200b5327124dee25759d4c19b9fdc54b8ec0493722c":
    raise SystemExit("Verification failed; no output written")
(root / "course-20261009-1000-evidence.zip").write_bytes(data)
print("Verified and restored course-20261009-1000-evidence.zip: 288608 bytes; SHA256 a529fceef00b7fd4263b8200b5327124dee25759d4c19b9fdc54b8ec0493722c")
