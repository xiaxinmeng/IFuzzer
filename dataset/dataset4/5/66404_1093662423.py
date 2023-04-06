import io, tarfile

with tarfile.open("foo.tar", mode="w") as tar:
    b = "hello world!".encode("utf-8")

    t = tarfile.TarInfo("helloworld.txt")
    t.size = len(b) # this is crucial
    tar.addfile(t, io.BytesIO(b))