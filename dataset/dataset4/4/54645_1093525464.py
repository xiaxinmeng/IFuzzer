# Create a simple tar file in memory.  This could easily be a real tar file
# though.
data = StringIO.StringIO()
tf = tarfile.open(fileobj=data, mode="w")
tarinfo = tarfile.TarInfo(name="testfile")
filedata = StringIO.StringIO("test data")
tarinfo.size = len(filedata.getvalue())
tf.addfile(tarinfo, fileobj=filedata)
tf.close()
data.seek(0)

# Open as an uncompressed stream
tf = tarfile.open(fileobj=data, mode="r|")