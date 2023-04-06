def f(x):
    y = x
    class Private:
        y = y
    return Private
f(17)