class A:
   def __getattr__(self, name):
     print(name)
     return A()


a=A()
a.foo
