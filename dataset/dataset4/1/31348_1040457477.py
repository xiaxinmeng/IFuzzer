
class A:
    def __dir__(self):
        return ['__class__', 'no_member']

obj = A()
inspect.getmembers_static(obj)      # ['__class__']
[(k, inspect.getattr_static(obj, k)) for k in dir(obj)] # AttributeError
