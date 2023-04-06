def f(items):
    if something:
        wrapper = int
    else:
        wrapper = identity

    for item in items:
        yield wrapper(item)