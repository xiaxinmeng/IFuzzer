def product(*args):
    if len(args) == 1:
        for i in args[0]:
            yield [i]
    else:
        for i in args[0]:
            for j in product(*args[1:]):
                j.append(i)
                yield j