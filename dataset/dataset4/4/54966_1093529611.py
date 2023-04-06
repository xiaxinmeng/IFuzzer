file = 'somefile.dat'
filename = "ółśąśółąś.dat"
zip = zipfile.ZipFile('archive.zip', 'w', zipfile.ZIP_DEFLATED)
zip.write(file, filename)