def __gen(exp):
    for _ in exp:
        yield next(F)

list(__gen(iter(range(10))))