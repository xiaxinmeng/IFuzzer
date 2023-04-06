from threading import local, Thread
from time import sleep

l = {}

def t0():
  b = l.get('e') # memory usage won't increase if I remove this line
  try:
    raise Exception('1')
  except Exception as e:
    l['e'] = e

def target():
  while True:
    sleep(0.0001)
    t0()

target()

# t = Thread(target=target)
# t.daemon = True
# t.start()