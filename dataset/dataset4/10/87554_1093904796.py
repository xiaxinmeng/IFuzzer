filesize = os.fstat(infd).st_size
offset = 0
while offset < filesize:
   sent = os.sendfile(outfd, infd, offset, blocksize)
   offset += sent