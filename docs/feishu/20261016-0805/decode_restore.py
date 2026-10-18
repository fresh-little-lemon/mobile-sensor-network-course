from pathlib import Path
import base64, hashlib
root = Path(__file__).resolve().parent
encoded = "".join((root / f"navigation-checkpoint.zip.base64.part{i}.txt").read_text().strip() for i in range(1, 3))
data = base64.b64decode(encoded, validate=True)
if len(data) != 477443 or hashlib.sha256(data).hexdigest() != "f87d5861bd15211987e124abd13ca9a4d4c23671667dcacdd251f12fe69717ba":
    raise SystemExit("Verification failed; no output written")
(root / "course-20261016-0805-navigation-checkpoint.zip").write_bytes(data)
print("Verified and restored course-20261016-0805-navigation-checkpoint.zip; SHA256 f87d5861bd15211987e124abd13ca9a4d4c23671667dcacdd251f12fe69717ba")
