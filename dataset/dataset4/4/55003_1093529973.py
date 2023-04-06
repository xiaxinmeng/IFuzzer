class A(object):
  def __init__(self):
    raise Exception('init error')
    self.m = 'Hello world'

  def __del__(self):
    #raise RuntimeError('my runtime error')
    self.__del__()

def func():
  h = A()

func()