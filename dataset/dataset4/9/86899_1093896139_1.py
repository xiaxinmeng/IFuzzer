
FILE_PATH = 'example.data'

# create a file
with open(FILE_PATH, 'w') as f:
    f.write('abc\n')

# Truncate using r+ mode.
with open(FILE_PATH, 'r+') as f:
    assert f.tell() == 0
    assert f.read() == 'abc\n'
    assert f.tell() == 4  # File position is now at end of file.
    f.truncate(0)
    assert f.tell() == 4  # File position has not changed.
    assert f.read() == ''  # Nothing remaining to read.
    f.write('xyz\n')
    f.flush()
    assert f.tell() == 8
    assert f.read() == ''  # Nothing remaining to read.
    # Return the file position to start of file.
    f.seek(0)
    assert f.read() == '\0\0\0\0xyz\n'

