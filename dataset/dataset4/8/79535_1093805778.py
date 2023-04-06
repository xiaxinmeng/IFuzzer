def foo():
    try:
        raise Exception()
    except:
        foo()
foo()