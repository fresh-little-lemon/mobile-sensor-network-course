from pathlib import Path
import base64, hashlib
root = Path(__file__).resolve().parent
encoded = "".join((root / f"navigation-checkpoint.zip.base64.part{i}.txt").read_text().strip() for i in range(1, 3))
data = base64.b64decode(encoded, validate=True)
if len(data) != 397030 or hashlib.sha256(data).hexdigest() != "69d11aaf6c83ff32c73aabcdc9b8fac3ac3321086bccc2533625e4a7f687d40f":
    raise SystemExit("Verification failed; no output written")
(root / "course-20261015-0803-navigation-checkpoint.zip").write_bytes(data)
print("Verified and restored course-20261015-0803-navigation-checkpoint.zip; SHA256 69d11aaf6c83ff32c73aabcdc9b8fac3ac3321086bccc2533625e4a7f687d40f")
