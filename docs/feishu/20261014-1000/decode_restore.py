from pathlib import Path
import base64, hashlib
root = Path(__file__).resolve().parent
encoded = "".join((root / f"navigation-checkpoint.zip.base64.part{i}.txt").read_text().strip() for i in range(1, 4))
data = base64.b64decode(encoded, validate=True)
if len(data) != 622870 or hashlib.sha256(data).hexdigest() != "d37464cc76ac7c94967883da708a3b4c4e03e4e4401e50c7ce50cc053ff004c6":
    raise SystemExit("Verification failed; no output written")
(root / "course-20261014-1000-navigation-checkpoint.zip").write_bytes(data)
print("Verified and restored course-20261014-1000-navigation-checkpoint.zip; SHA256 d37464cc76ac7c94967883da708a3b4c4e03e4e4401e50c7ce50cc053ff004c6")
