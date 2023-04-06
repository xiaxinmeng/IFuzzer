def test():
    for i in range(10):
        yield (square := i * i)