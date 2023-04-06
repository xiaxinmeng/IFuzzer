def f():
    try:
        return f()
    except:
        pass
    f()

f()