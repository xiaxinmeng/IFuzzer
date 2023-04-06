import sys

def overflower():
    try:
        return overflower()
    except:
        return sys.exc_info()


def f():
      try:
          return f()
      except:
          return overflower()

f()
######