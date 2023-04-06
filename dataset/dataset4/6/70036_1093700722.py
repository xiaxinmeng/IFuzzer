#!/usr/bin/python3.5
import tempfile

with tempfile.TemporaryFile(mode='r+t') as f:
    l = f.write('привет')
    print(l, f.tell()) # "6 12"
    f.seek(3)
    f.write('прекол42')
    f.seek(0)
    print(f.read()) # raise UnicodeDecodeError