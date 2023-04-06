import zipimport
zipimport._zip_directory_cache['foo.zip'] = None
importer = zipimport.zipimporter('foo.zip')
importer.find_loader('bar')