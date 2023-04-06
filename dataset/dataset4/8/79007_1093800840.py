import io
class X(io.RawIOBase):
  def readable(self):
    return True
  def readinto(self, b):
    if isinstance(b, memoryview):
      print(b.format)  # XXX boom, crashes here.
    return 0

io.BufferedReader(X()).read(8)