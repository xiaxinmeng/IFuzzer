class M1(type):
  pass

class M2(M1):
  pass

class C1(object):
  __metaclass__ = M1

class C2(C1):
  __metaclass__ = M2

class C3(C2):
  __metaclass__ = M1