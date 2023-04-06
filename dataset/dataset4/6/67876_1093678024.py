import gzip
x = memoryview(b'x' * 10)
y = x[::-1]
with gzip.GzipFile("xxxxx", 'w') as f:
    f.write(y)