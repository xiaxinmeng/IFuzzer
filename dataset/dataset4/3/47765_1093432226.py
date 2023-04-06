def foo():
    with open("a.txt", "w") as io:
        raise RuntimeError()