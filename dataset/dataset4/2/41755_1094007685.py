import zipfile
zipFile = zipfile.ZipFile("Test.zip", "w", zipfile.ZIP_DEFLATED)
zipFile.write(u"Test.bin")