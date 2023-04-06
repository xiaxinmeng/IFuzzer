import io
class A(io.RawIOBase):
  def readinto(self, b):
    return len(b)