if filename.endswith('.xz'):
    f = lzma.open(filename)
else:
    f = open(filename)
for line in f: ...