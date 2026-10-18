from pathlib import Path
import base64, hashlib
root = Path(__file__).resolve().parent
encoded = "".join((root / f"navigation-checkpoint.zip.base64.part{i}.txt").read_text().strip() for i in range(1, 3))
data = base64.b64decode(encoded, validate=True)
if len(data) != 321607 or hashlib.sha256(data).hexdigest() != "a14e9b497f395b5b0edb6eaf46032d141a0207d9ee81133f4c6e1fd709b1cab1":
    raise SystemExit("Verification failed; no output written")
(root / "course-20261013-1000-navigation-checkpoint.zip").write_bytes(data)
print("Verified and restored course-20261013-1000-navigation-checkpoint.zip; SHA256 a14e9b497f395b5b0edb6eaf46032d141a0207d9ee81133f4c6e1fd709b1cab1")
