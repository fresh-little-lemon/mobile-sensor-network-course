from pathlib import Path
import base64, hashlib
root = Path(__file__).resolve().parent
encoded = "".join((root / f"navigation-checkpoint.zip.base64.part{i}.txt").read_text().strip() for i in range(1, 2))
data = base64.b64decode(encoded, validate=True)
if len(data) != 263651 or hashlib.sha256(data).hexdigest() != "479cf497af4125b1b9f3948a2b86deba8cf0142a74059bffd3e479c5709555fe":
    raise SystemExit("Verification failed; no output written")
(root / "course-20261012-1620-navigation-checkpoint.zip").write_bytes(data)
print("Verified and restored course-20261012-1620-navigation-checkpoint.zip; SHA256 479cf497af4125b1b9f3948a2b86deba8cf0142a74059bffd3e479c5709555fe")
