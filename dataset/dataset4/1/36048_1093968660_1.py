import pickle
class A(long):
  pass

x = A(-1)
pickle.dumps(x)