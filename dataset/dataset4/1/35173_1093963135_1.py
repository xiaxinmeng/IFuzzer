f = gzip.open(filename, 'wb')
f.write(marshal.dumps(value))
f.close()