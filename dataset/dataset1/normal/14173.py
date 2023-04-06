#!/usr/bin/python
import signal

class foo(object):
  def __del__(self):
    signal.getsignal(signal.SIGHUP)

f=foo()
