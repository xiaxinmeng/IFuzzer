with zipfile.ZipFile("/tmp/dummy.zip", "w") as dummy:
    pass

def clone_zipfile(z):
    z_cloned = zipfile.ZipFile("/tmp/dummy.zip")
    z_cloned.NameToInfo = z.NameToInfo
    z_cloned.fp = open(z.fp.name, "rb")
    return z_cloned