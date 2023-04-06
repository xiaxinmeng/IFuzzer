import zipfile

file_zip = zipfile.ZipFile("test-one-dir.zip", mode='r')
for info in file_zip.infolist():
    print(info)