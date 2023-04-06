tar = tarfile.open("foo.tar.gz", "w:gz")
for filename in filenames:
  tarinfo = tar.gettarinfo(filename)
  if tarinfo.isreg():
    fobj = open(filename)
  else:
    fobj = None
  tarinfo.uid = 0
  tarinfo.gid = 0
  tar.addfile(tarinfo, fobj)
tar.close()