from pathlib import Path
import base64, hashlib
root = Path(__file__).resolve().parent
encoded = "".join((root / f"navigation-checkpoint.zip.base64.part{i}.txt").read_text().strip() for i in range(1, 3))
data = base64.b64decode(encoded, validate=True)
if len(data) != 361143 or hashlib.sha256(data).hexdigest() != "ab2290830b3f805e95fee1f3ad90d0d3be78d91860c315e2895d262c2586e2b0":
    raise SystemExit("Verification failed; no output written")
(root / "course-20261013-0803-navigation-checkpoint.zip").write_bytes(data)
print("Verified and restored course-20261013-0803-navigation-checkpoint.zip; SHA256 ab2290830b3f805e95fee1f3ad90d0d3be78d91860c315e2895d262c2586e2b0")
