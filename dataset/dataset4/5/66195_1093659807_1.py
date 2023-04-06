# Explicit dummy name to avoid using file name of bytes
tarinfo = self.tar.gettarinfo(fileobj=file, arcname="")
# . . .
tarinfo.name = "{}/{}".format(self.pkgname, name)