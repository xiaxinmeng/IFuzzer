class C1(object):
   def __new__(cls):
       return super(C1, cls).__new__(cls)

a = C1()