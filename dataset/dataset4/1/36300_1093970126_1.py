def f(x):
    y = x
    class Private:
        x = y
    return Private
f(17)