def outer():
    x = 1
    def inner1():
        print(x)
    def inner2():
        print(x)
        # [... some instructions (maybe a lot) ...]
        x = 1