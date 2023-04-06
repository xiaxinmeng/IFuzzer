class foo(object):
     a = 1
     b = [1,2,3]
     def __json__(self): return {'a':self.a,'b':self.b}