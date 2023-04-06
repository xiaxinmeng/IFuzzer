g = gzip.GzipFile(...)
r = io.BufferedReader(g)
for line in r:
    ...