import tarfile, io

with tarfile.open("sample.tar", mode="w") as tar:
    t = tarfile.TarInfo("foo")
    t.type = tarfile.DIRTYPE
    tar.addfile(t)

    b = "Hello world!".encode("ascii")

    t = tarfile.TarInfo("foo/bar")
    t.size = len(b)
    tar.addfile(t, io.BytesIO(b))