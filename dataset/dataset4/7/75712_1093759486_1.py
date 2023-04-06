import zipimport
importer = zipimport.zipimporter('foo.zip')
zipimport._zip_directory_cache['foo.zip']['foo\\__init__.py'] = None
importer.load_module('foo')