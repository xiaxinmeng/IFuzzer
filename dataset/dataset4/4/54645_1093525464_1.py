pytb
#f = tf.extractfile("testfile")
#print "%s: %s" % (f.name, f.read())
#
#Traceback (most recent call last):
#  File "./bug.py", line 19, in <module>
#    print "%s: %s" % (f.name, f.read())
#  File "/usr/lib/python2.7/tarfile.py", line 815, in read
#    buf += self.fileobj.read()
#  File "/usr/lib/python2.7/tarfile.py", line 735, in read
#    return self.readnormal(size)
#  File "/usr/lib/python2.7/tarfile.py", line 742, in readnormal
#    self.fileobj.seek(self.offset + self.position)
#  File "/usr/lib/python2.7/tarfile.py", line 554, in seek
#    raise StreamError("seeking backwards is not allowed")
#tarfile.StreamError: seeking backwards is not allowed
