class d(dict):
    _is_setted = None
    def __setitem__(self, k, v):
        self._is_setted = 1
 
class test:
    def __init__(self):
        self.__dict__ = d()
         
t = test()
t.x = 2
assert t.__dict__._is_setted == 1, 'no `__setitem__` calls'