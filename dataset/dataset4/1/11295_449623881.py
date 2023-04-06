def f(x, y, **kwargs):
    print(x, y)


def call_f():
    f(x=7, y=9, z=9)


call_f()