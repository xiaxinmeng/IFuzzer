import sys, os, threading, subprocess, time

class X(threading.Thread):
  def __init__(self, *args, **kwargs):
    super(X, self).__init__(*args, **kwargs)
    self.start()

def tt():
  s = subprocess.Popen(("/bin/ls", "-a", "/tmp"), stdout=subprocess.PIPE,
      universal_newlines=True)
  # time.sleep(1)
  s.communicate()[0]

for i in xrange(1000):
  X(target = tt)