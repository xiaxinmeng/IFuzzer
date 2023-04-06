class Base:
   def __init__(self, msg):
       self.msg = msg

   def __reduce__(self):
       return type(self), (self.msg,)

class Derived(Base):
   def __init__(self, a, b):
       super().__init__(f'{a}|{b}')

x = Derived('a', 'b')
assert x.msg == 'a|b'
y = pickle.dumps(x, -1)
z = pickle.loads(y)