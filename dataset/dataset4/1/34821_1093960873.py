from cStringIO import StringIO
from gzip import GzipFile

stringFile = StringIO()

gzFile = GzipFile("test1", 'wb', 9, stringFile)

gzFile.write('howdy there!')
r = gzFile.read()