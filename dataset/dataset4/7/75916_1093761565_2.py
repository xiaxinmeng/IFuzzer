# obj.d looks up d in the dictionary of obj
d = Obj.__dict__['d']

# If d defines the method __get__(),
if hasattr(d, '__get__'):

    # then d.__get__(obj) is invoked
    d.__get__(Obj)