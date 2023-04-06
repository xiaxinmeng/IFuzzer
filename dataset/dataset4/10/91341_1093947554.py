def f():
    try:
        print("raise")
        raise ValueError
    except ValueError:
        print("except")
    else:
        print("else")
    print("exit func")

def g(): pass

if 1:
    code = f.__code__
    g.__code__ = g.__code__.replace(
        co_code=code.co_code,
        co_consts=code.co_consts,
        co_names=code.co_names,
        co_flags=code.co_flags,
        co_stacksize=code.co_stacksize)
else:
    g.__code__ = f.__code__  # this code path works on Python 3.11

g()