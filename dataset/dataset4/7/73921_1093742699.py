def decorator(f):
    def wrapper(*args):
        return f(*args)
    return wrapper

def f(*args): pass

for i in range(n):
    f = partial(f)
    f = decorator(f)

f(1, 2)