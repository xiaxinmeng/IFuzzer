def inf():
  for i in range(0,100): yield 0

def use(*parm):
  for i in parm: print(i)
use(*inf())
