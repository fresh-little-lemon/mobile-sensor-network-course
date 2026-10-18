from pathlib import Path
import base64, hashlib
root = Path(__file__).resolve().parent
encoded = "".join((root / f"evidence.zip.base64.part{i}.txt").read_text().strip() for i in range(1, 2))
data = base64.b64decode(encoded, validate=True)
if len(data) != 146227 or hashlib.sha256(data).hexdigest() != "691e42b6ba0e791b58f4c2c03b7a466adb82ba4051eb78c26fc86f3d6a6b9c3f":
    raise SystemExit("Verification failed; no output written")
(root / "course-20261009-0759-evidence.zip").write_bytes(data)
print("Verified and restored course-20261009-0759-evidence.zip: 146227 bytes; SHA256 691e42b6ba0e791b58f4c2c03b7a466adb82ba4051eb78c26fc86f3d6a6b9c3f")
