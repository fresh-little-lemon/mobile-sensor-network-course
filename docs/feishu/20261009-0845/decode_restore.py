from pathlib import Path
import base64, hashlib
root = Path(__file__).resolve().parent
encoded = "".join((root / f"evidence.zip.base64.part{i}.txt").read_text().strip() for i in range(1, 2))
data = base64.b64decode(encoded, validate=True)
if len(data) != 182360 or hashlib.sha256(data).hexdigest() != "ddc772961a027e81cd4d419114ef197fb881ef40c7210adff184637363f88a8e":
    raise SystemExit("Verification failed; no output written")
(root / "course-20261009-0845-evidence.zip").write_bytes(data)
print("Verified and restored course-20261009-0845-evidence.zip: 182360 bytes; SHA256 ddc772961a027e81cd4d419114ef197fb881ef40c7210adff184637363f88a8e")
