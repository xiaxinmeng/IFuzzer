class foo(object):
  class __metaclass__(type):
    def __new__(cls, name, bases, dict):
      return type.__new__(cls, name, bases, dict)