
import zipfile

try:
    import zipp
except ImportError:
    import zipfile as zipp

zip_file = zipfile.ZipFile('zipfile.zip')
name = zip_file.namelist()[0]
zipp.Path(zip_file)
zip_file.open(name)
