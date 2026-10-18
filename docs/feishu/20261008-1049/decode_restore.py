from pathlib import Path
import base64, hashlib
root = Path(__file__).resolve().parent
encoded = "".join((root / f"evidence.zip.base64.part{i}.txt").read_text().strip() for i in range(1, 2))
data = base64.b64decode(encoded, validate=True)
if len(data) != 197686 or hashlib.sha256(data).hexdigest() != "97a1871f0a3a1ad21d5d2244b51dff89701ee73010d3e3d6d8948682125acc63":
    raise SystemExit("Verification failed; no output written")
(root / "course-20261008-1049-evidence.zip").write_bytes(data)
print("Verified and restored course-20261008-1049-evidence.zip: 197686 bytes; SHA256 97a1871f0a3a1ad21d5d2244b51dff89701ee73010d3e3d6d8948682125acc63")
