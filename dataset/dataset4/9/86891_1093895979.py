def foo():
    for number in range(5):
        foo: (yield number)
    return number

foo()