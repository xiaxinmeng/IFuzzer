def f():
    if random.random() < 0.5:
        a = 1
        b = 2
    else:
        b = 1
        a = 2
    return locals()