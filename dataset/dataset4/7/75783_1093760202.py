import zlib
import zipimport
def bad_decompress(*args):
    return None

zlib.decompress = bad_decompress
zipimport.zipimporter('foo.zip').get_source('bar')