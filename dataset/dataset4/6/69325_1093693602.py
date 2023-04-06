# Check for internet access before running test (issue python/cpython#57013).
with support.transient_internet('python.org'):
    socket.gethostbyname('python.org')
# these should all be successful
...