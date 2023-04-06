def decorator():
    def inner(f):
        def wrapper(*args, **kwargs):
            # Zoinks, Scoob!
            print('Decorator: {}'.format(''.join(kwargs.values())))
            print(f(*args, **kwargs))
        return wrapper
    return inner

@decorator()
def func(foo='wont print in the decorator'):