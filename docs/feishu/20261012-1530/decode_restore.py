from pathlib import Path
import base64, hashlib
root = Path(__file__).resolve().parent
encoded = "".join((root / f"navigation-checkpoint.zip.base64.part{i}.txt").read_text().strip() for i in range(1, 2))
data = base64.b64decode(encoded, validate=True)
if len(data) != 202933 or hashlib.sha256(data).hexdigest() != "533528e810970b4779ca69e51e2e73b041a90fbcb73c4516d18f5e929c2985f8":
    raise SystemExit("Verification failed; no output written")
(root / "course-20261012-1530-navigation-checkpoint.zip").write_bytes(data)
print("Verified and restored course-20261012-1530-navigation-checkpoint.zip; SHA256 533528e810970b4779ca69e51e2e73b041a90fbcb73c4516d18f5e929c2985f8")
