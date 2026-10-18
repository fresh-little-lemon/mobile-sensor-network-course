from pathlib import Path
import base64, hashlib
root = Path(__file__).resolve().parent
encoded = "".join((root / f"evidence.zip.base64.part{i}.txt").read_text().strip() for i in range(1, 2))
data = base64.b64decode(encoded, validate=True)
if len(data) != 192788 or hashlib.sha256(data).hexdigest() != "b7b5746eef328410aa43dddc117be850693db24d1e6ae570244155abb5d5818b":
    raise SystemExit("Verification failed; no output written")
(root / "course-20261008-1000-evidence.zip").write_bytes(data)
print("Verified and restored course-20261008-1000-evidence.zip: 192788 bytes; SHA256 b7b5746eef328410aa43dddc117be850693db24d1e6ae570244155abb5d5818b")
