
import tarfile
c = io.BytesIO()
with tarfile.open(mode='w', fileobj=c) as tar:
  for textfile in ['1.txt.gz', '2.txt.gz']:
    with gzip.open(textfile) as f:
      tarinfo = tar.gettarinfo(fileobj=f)
      tar.addfile(tarinfo=tarinfo, fileobj=f)
  data = c.getvalue()
return data
