test2 = functools.partial(test, a=10)

@functools.wraps(test)
def test2():
    return test(a=10)