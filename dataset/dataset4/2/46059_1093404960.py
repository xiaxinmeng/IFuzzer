import tarfile

f = file(r"nss-3.12_alpha2.tar.bz2", "rb")
tar = tarfile.open(fileobj=f, mode="r|bz2")
try:
        for m in tar:
                tar.extract(m)
finally:
        tar.close()
        f.close()