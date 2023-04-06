import zipfile
import os

allFilesToZip = ["/tmp/tom"]

with zipfile.ZipFile(allZipPath, 'w') as allZip:
    for f in allFilesToZip:
        allZip.write(f, compress_type=zipfile.ZIP_DEFLATED)
    for zip_info in allZip.infolist():
        if zip_info.filename[-1] == '/':
            continue
        zip_info.filename = os.path.basename(zip_info.filename)