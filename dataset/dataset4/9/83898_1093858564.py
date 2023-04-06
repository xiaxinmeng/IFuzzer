def f(x, y):
    "Return (x+y)/y for non-zery y."

    if y == 0:  # Body 1: look ahead.
        raise ValueError('y cannot be 0')
    else:
        return (x+y)/y
# or
    try:  # Body 2: leap first.
        return (x+y)/y
    except ZeroDivisionError:
        raise ValueError('y cannot be 0') from None