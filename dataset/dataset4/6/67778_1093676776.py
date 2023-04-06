import sys, time
class C(object):
  def __float__(self):
    return ""
for x in range(10000):
  try:
    time.sleep(C())
  except TypeError:
    pass
  if x % 1000 == 0:
    print(sys.getrefcount(""))