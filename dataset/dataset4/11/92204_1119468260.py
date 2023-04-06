def makecode():
    x = 1
    return (lambda: x*x).__code__

eval(makecode())