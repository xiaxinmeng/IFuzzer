def f():
    C = None
    def g():
        nonlocal C
        class C: pass
    return g()