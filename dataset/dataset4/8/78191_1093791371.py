# read with tarfile as stream (note pipe symbol in 'r|gz')
import tarfile
tfile = tarfile.open("test.tgz", 'r|gz')
for t in tfile:
    file = tfile.extractfile(t)
    if file:
        print(len(file.read()))