f = gzip.open(filename, 'wb')
marshal.dump(value, f)
f.close()