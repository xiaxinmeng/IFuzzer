import tempfile
import marshal
tmpfile = tempfile.TemporaryFile(mode='w+b')
# TypeError: marshal.dump() 2nd arg must be file
marshal.dump({}, tmpfile)