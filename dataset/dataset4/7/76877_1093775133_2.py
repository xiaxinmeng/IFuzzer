class Derived(Base):
   def __init__(self, a, b):
       super().__init__(f'{a}|{b}')

   def __reduce__(self):
       return type(self), tuple(self.msg.split('|'))