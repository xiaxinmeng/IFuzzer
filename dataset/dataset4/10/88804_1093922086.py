
zip_file = zipfile.ZipFile('zipfile.zip')
path = zipfile.Path(zip_file)
name = zip_file.namelist()[0]
del path
zip_file.open(name)
