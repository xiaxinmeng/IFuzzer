def f(self): ...   # not even defined inside a class
A.f = f            # stored in class A
B.f = f            # also stored in class B
dir(f)             # f doesn't know where it is stored