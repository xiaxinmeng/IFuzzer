def roundrobin(*iters):
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
    # Perhaps "flat_zip_nofill" is a better name, or something similar
    sentinel = object()
    for tup in it.zip_longest(*iters, fillvalue=sentinel):
        yield from (x for x in tup if x is not sentinel)