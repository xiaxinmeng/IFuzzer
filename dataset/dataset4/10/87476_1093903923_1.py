
class A:
   my_del = lambda *args, **kwargs: None
   def __del__(self):
       self.my_del(self)
A.my_del = C()
