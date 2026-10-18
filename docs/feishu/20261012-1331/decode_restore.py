from pathlib import Path
import base64, hashlib
root = Path(__file__).resolve().parent
encoded = "".join((root / f"evidence.zip.base64.part{i}.txt").read_text().strip() for i in range(1, 2))
data = base64.b64decode(encoded, validate=True)
if len(data) != 235245 or hashlib.sha256(data).hexdigest() != "327e02f6d9ebdb1739a6789d4b30d342ee351cda2d419788282d1a56c41c82de":
    raise SystemExit("Verification failed; no output written")
(root / "course-20261012-1331-evidence-asr-pending.zip").write_bytes(data)
print("Verified and restored course-20261012-1331-evidence-asr-pending.zip: 235245 bytes; SHA256 327e02f6d9ebdb1739a6789d4b30d342ee351cda2d419788282d1a56c41c82de")
