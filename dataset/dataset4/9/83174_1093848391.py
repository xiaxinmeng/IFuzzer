import functools
import cProfile

def decor(func):
    @functools.wraps(func)
    def wraps(*args, **kwargs):
        return func(*args, **kwargs)
    return wraps

@decor
def count(g_val):
    if g_val < 1:
        print("End")
    else:
        count(g_val - 1)
 
cProfile.run('count(102)')