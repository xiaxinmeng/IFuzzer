def cat(fnames):
    lines = chain.from_iterable(itercm(open(f)) for f in fnames)
    for line in lines:
        print(line, end='')