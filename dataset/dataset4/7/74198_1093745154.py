if sys.version_info >= (3,):
    handle = gzip.open(filename, "rt")
else:
    handle = gzip.open(filename)