def identity_dec(func):
    def wrapper(*args, **kw):
        return func(*args, **kw)
    return functools.update_wrapper(wrapper, func)

@identity_dec
def example(): 
    pass