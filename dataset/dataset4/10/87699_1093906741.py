
import contextlib
import gc

@contextlib.contextmanager
def ct():
  yield


class A(object):

  def __getattr__(self, name):
    with ct():
      raise AttributeError()
  


def f():
  a = A()
  hasattr(a, 'notexist')


gc.set_debug(gc.DEBUG_LEAK)
f()
gc.collect()
