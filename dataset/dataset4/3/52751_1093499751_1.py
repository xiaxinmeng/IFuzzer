def setup(testobj):
    """Test setup."""
    # Make sure future statements in our doctests match the Python code.
    testobj.globs['absolute_import'] = absolute_import
    testobj.globs['unicode_literals'] = unicode_literals