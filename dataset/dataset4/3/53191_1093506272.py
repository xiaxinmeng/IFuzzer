class A(object):
     def keys(self): return list("ab")
     def __getitem__(self, key):
         return 42
        
class B(dict):
     def keys(self): return list("ab")
     def __getitem__(self, key):
         return 42

def f(**kw):
     print(kw)

f(**A())
# {'a': 42, 'b': 42}

b = B(); print(b['a'], b['b']) # I added this
# 42, 42
f(**b)
# {}