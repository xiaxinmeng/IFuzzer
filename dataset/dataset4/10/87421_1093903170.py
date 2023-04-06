def ceil_div(x, y):
    rem=x % y
    if rem:
        x += y - rem
    return x//y