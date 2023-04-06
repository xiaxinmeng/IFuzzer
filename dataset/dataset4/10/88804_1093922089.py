
zip_file = zipfile.ZipFile('zipfile.zip')
name = zip_file.namelist()[0]
zipfile.Path(zip_file)
zip_file.open(name)
