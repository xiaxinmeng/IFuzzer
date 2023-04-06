
import fileinput
import bz2
import pathlib

target = pathlib.Path('data.bz2')
target.write_bytes(bz2.compress(b'Foo\nBar\nBiz'))

inp = fileinput.FileInput([str(target)], openhook=fileinput.hook_compressed)
for line in inp:
    print(line.decode().strip())
