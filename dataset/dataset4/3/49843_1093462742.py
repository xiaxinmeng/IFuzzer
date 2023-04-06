def add(x, y):
    return x + y

if add(1e16, 2.0) != add(1e16, 2.9999):
    return