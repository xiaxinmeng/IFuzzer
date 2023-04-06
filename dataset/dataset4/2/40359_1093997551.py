def yield_line_and_islastline(f):
    try:
        prevline = next(f)
    except StopIteration:
        return
    for line in f:
        yield (prevline, f.isfirstline())
        prevline = line
    yield prevline, True