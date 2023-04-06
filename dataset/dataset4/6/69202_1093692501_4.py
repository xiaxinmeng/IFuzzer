def lazy_cat(fnames):
    for fname in fnames:
        with open(fname) as f:
            yield from f