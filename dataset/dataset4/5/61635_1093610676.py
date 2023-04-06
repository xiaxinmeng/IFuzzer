def report_first_ten(g):
    s = itertools.islice(g, 10)
    yield from s
    print("First 10 done.")
    yield from g