from zipfile import ZipFile
import tempfile
temporary_file = tempfile.NamedTemporaryFile()
my_zip = ZipFile(temporary_file.name, 'w')
my_zip.writestr('/some_folder/some_file.txt', 'Some content')
my_zip.close()