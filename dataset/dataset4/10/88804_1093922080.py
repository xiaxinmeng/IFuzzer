
import zipfile


zip_file = zipfile.ZipFile('zipfile.zip')
names = [each.name for each in zipfile.Path(zip_file).iterdir()]
with zip_file.open(names[0]) as file:
    print(file.read())
