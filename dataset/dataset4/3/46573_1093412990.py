import sys, os, threading, subprocess, time

class X(threading.Thread):
  def __init__(self, *args, **kwargs):
    super(X, self).__init__(*args, **kwargs)
    self.start()

def tt():
  s = subprocess.Popen(("cat"), stdin=subprocess.PIPE)
  s.communicate(input = '#')

for i in xrange(20):
  X(target = tt)