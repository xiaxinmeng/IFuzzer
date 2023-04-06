import zipfile, os

filename="test.zip" # it's a broken one
try:
  zf=zipfile.ZipFile(filename)
  zf.close()
finally:
  os.unlink(zipfile)