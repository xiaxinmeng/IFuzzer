import tempfile

with tempfile.SpooledTemporaryFile(mode='wt') as f:
    f.write('abc')
    assert f._file.getvalue() == 'abc'