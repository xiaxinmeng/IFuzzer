import tarfile, io

fileToAdd = io.BytesIO("hello world!".encode("utf-8"))
with tarfile.open("sample.tar", mode="w") as tar:

    # this TarInfo object has:
    #    name = 'somefile.txt'
    #    type = REGTYPE (or whatever is 'just a regular file')
    #    uid = 501, gid = 20, gname=staff, uname=markgrandi, mode=644
    tmpTarInfo = tar.gettarinfo("somefile.txt", fileToAdd)
    tar.addfile()