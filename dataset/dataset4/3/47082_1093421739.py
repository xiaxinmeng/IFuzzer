def except_yield():
    try:
        raise Exception("foo")
    except:
        yield 1
        raise
list(except_yield())