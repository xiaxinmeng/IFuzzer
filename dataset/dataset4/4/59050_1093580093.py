def five(x):
    "Generator yields the object x five times."
    for _ in range(5):
        yield x