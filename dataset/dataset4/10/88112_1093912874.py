
import pickle

class MyList(list):
  def __init__(self, required, values):
    self.required = required
    super().__init__(values)

  def __getstate__(self):
    return self.required

  def __setstate__(self, state):
    self.required = state

  def extend(self, values):
    assert self.required
    super().extend(values)

mylist = MyList('foo', [1, 2])
pickled = pickle.dumps(mylist)
unpickled = pickle.loads(pickled)

print(mylist)

