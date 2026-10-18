from pathlib import Path
import base64, hashlib
root = Path(__file__).resolve().parent
encoded = "".join((root / f"evidence.zip.base64.part{i}.txt").read_text().strip() for i in range(1, 2))
data = base64.b64decode(encoded, validate=True)
if len(data) != 250096 or hashlib.sha256(data).hexdigest() != "528c442682e0d33e157d6778c76fe3dd1c08b1c62cb46e7c401c72e770714765":
    raise SystemExit("Verification failed; no output written")
(root / "course-20261008-0800-evidence.zip").write_bytes(data)
print("Verified and restored course-20261008-0800-evidence.zip: 250096 bytes; SHA256 528c442682e0d33e157d6778c76fe3dd1c08b1c62cb46e7c401c72e770714765")
