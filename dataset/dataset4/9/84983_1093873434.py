def x(y):
    while True:
        yield y

p = product(x(1), x(2))

next(p)  # this string will never be reached.