from pathlib import Path
import base64, hashlib
root = Path(__file__).resolve().parent
encoded = "".join((root / f"navigation-checkpoint.zip.base64.part{i}.txt").read_text().strip() for i in range(1, 3))
data = base64.b64decode(encoded, validate=True)
if len(data) != 322896 or hashlib.sha256(data).hexdigest() != "972d2e3d94fa564535ce79eb895ee10ea5873db923ec71be8fddbb9cd7f60ca3":
    raise SystemExit("Verification failed; no output written")
(root / "course-20261014-0801-navigation-checkpoint.zip").write_bytes(data)
print("Verified and restored course-20261014-0801-navigation-checkpoint.zip; SHA256 972d2e3d94fa564535ce79eb895ee10ea5873db923ec71be8fddbb9cd7f60ca3")
