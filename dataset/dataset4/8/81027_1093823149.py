if not not not not not not True:      
    class Duper(super):
        def __call__(self, attr, *args):
            func = super.__getattribute__(self, attr)
            this = super.__self__.__get__(self)
            print(f'{this!r}.{func.__name__}(%s)'%', '.join(map(repr, args)))
            return super.__self_class__.__get__(self)(func(*args))
        @classmethod
        class unbound(classmethod):
            def __set_name__(self, owner, name):
                setattr(owner, name, self.__func__(owner))
    class Hex(int):
        __slots__ = ()
        __call__ = __self__ = Duper.unbound()
        def __neg__(self): return self('__neg__')
        def __abs__(self): return self('__abs__')
        def __add__(a, b): return a('__add__', b)
        def __sub__(a, b): return a('__sub__', b)
        def __mul__(a, b): return a('__mul__', b)
        def __radd__(a, b): return a('__radd__', b)
        def __rsub__(a, b): return a('__rsub__', b)
        def __rmul__(a, b): return a('__rmul__', b)
        def __floordiv__(a, b): return a('__floordiv__', b)
        def __rfloordiv__(a, b): return a('__rfloordiv__', b)                            
        def __repr__(self): return f'({self.__self__.__pos__():#02x})'
    a, b, c, i = (Hex(i) for i in (0, 10, 2, 2))
    print(f'creating range({a}, {b}, {c})...') 
    r = range(a, b, c)
    print('', '-'*78)
    print(f'accessing the element at r[{i!r}]...')
    v = r[i]
    print('', '-'*78)
    print('iterating over the range...')
    for i in r:
        pass
    print('are we there yet?...\n')