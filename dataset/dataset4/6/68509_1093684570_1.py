def f():
    x = None
    def g():
        nonlocal x
        with open("/dev/null") as x:
            pass
    g()
    print("x", x)
f()