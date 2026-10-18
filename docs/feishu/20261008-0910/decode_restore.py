from pathlib import Path
import base64, hashlib
root = Path(__file__).resolve().parent
encoded = "".join((root / f"evidence.zip.base64.part{i}.txt").read_text().strip() for i in range(1, 2))
data = base64.b64decode(encoded, validate=True)
if len(data) != 112836 or hashlib.sha256(data).hexdigest() != "a40ccb39ebba0948d0fc271be367eb04878695574369f2f7511dcd17d60b3cf3":
    raise SystemExit("Verification failed; no output written")
(root / "course-20261008-0910-evidence.zip").write_bytes(data)
print("Verified and restored course-20261008-0910-evidence.zip: 112836 bytes; SHA256 a40ccb39ebba0948d0fc271be367eb04878695574369f2f7511dcd17d60b3cf3")
