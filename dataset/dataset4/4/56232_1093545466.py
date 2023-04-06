def nok():
    a = None
    def f():
        if a:
            a = 1
    f()

def ok():
    a = None
    def f():
        if a:
            b = 1
    f()