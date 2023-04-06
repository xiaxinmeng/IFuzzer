
def f1():
  sys._getframe(1).f_locals.update({'a':3, 'b':4})
  print(a, b)

f1()
