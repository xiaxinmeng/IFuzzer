from bar import bar

def foo():
    bar()

def nope():
    pass

def foobar():
    foo()
    nope()

foobar()