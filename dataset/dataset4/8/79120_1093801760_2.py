
def outer():
    def inner():
        nonlocal y
        y = 1
    y:int = 0
