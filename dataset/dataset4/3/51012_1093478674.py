class Broken():
  def __init__(self):
    break_it()

def break_it():
  Broken()

from threading import Thread
threads = [Thread(target=break_it) for x in range(100)]
for t in threads: t.start()