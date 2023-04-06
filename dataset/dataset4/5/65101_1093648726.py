class MyObj:
  def __init__(self, key, value):
     self.key = key
     self.value = value
  def __key(self):
    return self.key
  def __hash__(self):
    return hash(self.__key())
  def __eq__(self, other):
    return type(self) is type(other) and self.__key() == other.__key()

a = {MyObj(1, 'a')}

b = {MyObj(1, 'b')}