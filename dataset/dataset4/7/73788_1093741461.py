class C(object):
  def __init__(self, x):
     self.x = x
  def __complex__(self):
    return self.x

x=C(-0j)