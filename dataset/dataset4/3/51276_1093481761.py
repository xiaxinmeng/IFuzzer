import codecs, _codecs, sys, encodings

encoding = "cp1252"

codec = _codecs.lookup(encoding)

modname = 'encodings.%s' % encoding
__import__(modname)
del sys.modules[modname]
delattr(encodings, encoding)

encoder = codecs.getincrementalencoder(encoding)()
encoder.encode("", True)