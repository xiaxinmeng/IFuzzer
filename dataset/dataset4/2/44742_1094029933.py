class a(object):
   def __init__(self, foo):
       super(a, self).__init__(foo)
   def __new__(cls, foo):
       return object.__new__(cls)
a(1)