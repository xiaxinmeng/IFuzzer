data = BytesIO()
writer = tarfile.TarFile(fileobj=data, mode='w')
selflink = tarfile.TarInfo('self')
selflink.size = 0
selflink.type = tarfile.SYMTYPE
selflink.linkname = selflink.name
writer.addfile(selflink)
writer.close()
data.seek(0)
tarfile.TarFile(fileobj=data).extractall()