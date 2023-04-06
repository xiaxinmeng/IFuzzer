import tarfile

fname = unichr(40960) + u"a.ogg"

f = file(fname, "w")
f.write("A")
f.close()
        
tar_pipe = tarfile.open("test.tar", mode="w|",
    format=tarfile.PAX_FORMAT)
tar_pipe.add(fname)
tar_pipe.close()

tar_pipe = tarfile.open("test.tar")
tar_pipe.extractall(u".") # Just "." as string works fine.