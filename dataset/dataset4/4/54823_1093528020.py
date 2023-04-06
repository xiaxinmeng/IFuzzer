zipfile.ZipFile("non-ascii-cp932.zip", filename_encoding="cp932")

f = zipfile.ZipFile("test.zip", "w")
f.write(filename, filename_encoding="UTF-8")
info = ZipInfo(filename, filename_encoding="UTF-8")
f.writestr(info, b'data')