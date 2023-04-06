import tarfile
f = tarfile.open("test.tgz", mode="w:gz")
f.close()