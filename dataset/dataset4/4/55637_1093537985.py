class MakeContextHandler:
  def __init__(self, enter, exit):
    self.__enter__ = enter
    self.__exit__ = exit

with MakeContextHandler(lambda: None, lambda *e: None): pass