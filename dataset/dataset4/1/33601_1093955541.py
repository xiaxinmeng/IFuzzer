def make_adder(x):
    def adder(y):
        return x + y
    return adder
dec = make_adder(-1)
dec(1) == 0