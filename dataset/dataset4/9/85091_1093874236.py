import tarfile
out = tarfile.open(name="./t2.tar", mode="w", format=tarfile.PAX_FORMAT)
with tarfile.open("./t1.tar") as tar:
    for file in tar.getmembers():
        print (file.name)
        out.addfile(file)
out.close()