class restartable:
  def __init__(self, genfn):
    self.genfn = genfn
  def __call__(self, *args):
    return restartable_generator(self.genfn, *args)

class restartable_generator:
  def __init__(self, genfn, *args):
    self.genfn = genfn
    self.args = args
  def __iter__(self):
    return self.genfn(*self.args)