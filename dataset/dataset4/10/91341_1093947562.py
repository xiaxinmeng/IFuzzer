def f():
    foo()
    try:
        bar()
    except:
        pass

def g():
    try:
        foo()
        bar()
    except:
        pass