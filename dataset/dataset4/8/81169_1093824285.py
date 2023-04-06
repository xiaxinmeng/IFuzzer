import zipfile
import sys

zf = zipfile.ZipFile(sys.argv[1])
for info in zf.infolist():
  zf.extract(info.filename)