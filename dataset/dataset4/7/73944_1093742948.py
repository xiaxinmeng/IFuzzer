
def mappedclass(old_cls):
    '''
    Ensures that objects returned from functions in the clipper_core
    library are instantiated in Python as the derived class with the
    extra functionality. 
    '''
    def decorator(cls):
        def __newnew__(thiscls, *args, **kwargs):
            if thiscls == old_cls:
                return object.__new__(cls)
            return object.__new__(thiscls)
        old_cls.__new__ = __newnew__
        
        return cls
    return decorator

@mappedclass(foobar.Foo)
class Foo(foobar.Foo):
    pass

@mappedclass(foobar.Bar)
class Bar(foobar.Bar):
    def get_foo(self):
        return super(Bar, self).get_foo()

