def g0():
    return (yield from ())  # Immediately raise StopIteration(None).