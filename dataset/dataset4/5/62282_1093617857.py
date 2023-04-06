import io 
class A(io.IOBase): 
  def __init__(self): 
    self.x = 5 
  def read(self, limit=-1): 
    self.x -= 1 
    if self.x > 0: 
      return b"5" 
    return b"" 
  def seek(self, offset, whence=0): 
    return 0 
  def write(self, b): 
    pass 
 
a = A() 
a.close() 
assert a.__next__() == b"5555" 
assert a.readline() == b"" 
assert a.tell() == 0