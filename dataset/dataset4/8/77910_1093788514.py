from hashlib import blake2b
print (blake2b(b"foobar").hexdigest()) # works
print (blake2b(data=b"foobar").hexdigest()) # TypeError: 'data' is an invalid keyword argument for this function