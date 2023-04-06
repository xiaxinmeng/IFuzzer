
x = 1
def foo():
    # global x
    x = 1
    def bar():
        print(locals())
        y = x
    bar()
foo()
