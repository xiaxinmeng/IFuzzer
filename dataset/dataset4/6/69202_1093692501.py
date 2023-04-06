with open(fname) as f:
    transformed = (transform(line) for line in f)
    filtered = (line for line in lines if filter(line))
    # ...