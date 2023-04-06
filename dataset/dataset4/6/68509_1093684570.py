def f():
    x = None
    def g():
        nonlocal x
        try:
            raise Exception()
        except Exception as x:
            pass
    g()
    # ↓ UnboundLocalError: local variable 'x' referenced before assignment
    print("x", x)
f()