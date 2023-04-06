def skipUnlessCompressionModule(name):
    """
    Skip if the specified compression module is not available.  Must e a
    string, currently any of 'gzip', 'bz2', or 'lzma'.
    """
    return unittest.skipUnless(globals()[name],
                               '{} not available'.format(name))