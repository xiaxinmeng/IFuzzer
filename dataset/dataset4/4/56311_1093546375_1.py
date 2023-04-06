import mmap
from tempfile import TemporaryFile

f = TemporaryFile()
f.write(b"hello world")