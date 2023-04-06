f = zf.open(zinfo.filename, "r")
while f.read( 2 ** 20):     # Check CRC-32
  pass
f.close()
f._fileobj.close() # This shoulnd't be necessary, but it is.