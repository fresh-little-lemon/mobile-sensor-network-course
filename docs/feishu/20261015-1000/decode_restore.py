from pathlib import Path
import base64, hashlib
root = Path(__file__).resolve().parent
encoded = "".join((root / f"navigation-checkpoint.zip.base64.part{i}.txt").read_text().strip() for i in range(1, 3))
data = base64.b64decode(encoded, validate=True)
if len(data) != 531176 or hashlib.sha256(data).hexdigest() != "00f0bf9ca8c99616fef079e15764ee46760d90e5f741c8aaae3049a0cf87468d":
    raise SystemExit("Verification failed; no output written")
(root / "course-20261015-1000-navigation-checkpoint.zip").write_bytes(data)
print("Verified and restored course-20261015-1000-navigation-checkpoint.zip; SHA256 00f0bf9ca8c99616fef079e15764ee46760d90e5f741c8aaae3049a0cf87468d")
