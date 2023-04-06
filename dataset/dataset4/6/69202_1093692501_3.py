def lazy_cat(fnames):
    for fname in fnames:
        yield from itercm(open(fname))