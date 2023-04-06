# a.py
time.sleep(10)
import b

# b.py
time.sleep(10)
import a

# main.py
def x():
  import a
def y():
  import b