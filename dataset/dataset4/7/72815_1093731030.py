gen = (2**i for i in itertools.count())
next(gen)  # Generator suspended but won’t catch any exception
del gen  # Like deleting a plain iterator; no ResourceWarning expected