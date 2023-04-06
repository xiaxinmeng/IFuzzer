f = itercm(open(fname))
transformed = (transform(line) for line in f)
filtered = (line for line in lines if filter(line))
...
# someone consumes filtered down the line lazily
# and eventually the file gets closed