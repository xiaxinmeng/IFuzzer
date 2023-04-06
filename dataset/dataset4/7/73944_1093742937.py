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
 
def getters_to_properties(*funcs):
    '''
    Class decorator. Add the names of any getter functions with void 
    arguments (e.g. Coord_grid.u()) to convert them to properties. If
    you want the property name to be different from the function name,
    add the desired name and the function name as a tuple 
    (e.g. ('uvw', '_get_uvw'))
    '''
    def property_factory(func):
        def getter(self):
            return getattr(super(self.__class__, self), func)()
        prop = property(getter)
        return prop

    def decorator(cls):
        for func in funcs:
            if type(func) == tuple:
                setattr(cls, func[0], property_factory(func[1]))
            else:
                setattr(cls, func, property_factory(func)) 
        return cls
    return decorator

def format_to_string(cls):
    '''
    Class decorator to redirect the Clipper format() function to __str__,
    to provide pretty printing of the object.
    '''
    def format(self):
        return super(self.__class__,self).format()
    def __str__(self):
        return self.format
    setattr(cls, 'format', property(format))
    setattr(cls, '__str__', __str__)
    return cls