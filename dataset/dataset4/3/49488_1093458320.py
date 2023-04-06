import ssl

# Work around python bug python/issues-test-cpython#5328
def SSLSocket_makefile_fixed(self, mode='r', bufsize=-1):
    from socket import _fileobject