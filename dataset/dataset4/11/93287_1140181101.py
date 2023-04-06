import io
path = 'gh93287.dat'
with open(path, 'wb') as f:
    f.truncate(18+2297167872)

with open(path, 'rb') as f:
    data = f.read(18)
    assert len(data) == 18
    length = f.seek(0, io.SEEK_END)
    assert length == 18+2297167872
    f.seek(18, io.SEEK_SET)
    data = f.read(2297167872)
    assert len(data) == 2297167872