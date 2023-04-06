from tempfile import SpooledTemporaryFile

def _seekable(self):
    """
    Monkey patched seekable() method for the SpooledTemporaryFile class.

    Sadly, we cannot send an instance of the SpooledTemporaryFile to the
    ZipFile object.

    This is because the SpooledTemporaryFile doesn't inherit / implement the
    IOBase class.

    This bug is reported in CPython:

        https://bugs.python.org/issue26175

    And an unmerged PR is located here:

        https://github.com/python/cpython/pull/3249/files

    In Python 3.8, attempting to pass the tmpfd fails with:

        AttributeError:
            'SpooledTemporaryFile' object has no attribute 'seekable'

    So, the workaround to avoid copying the file is to monkey patch the class 
    and add the missing method. Sorry.
    """
    return self._file.seekable()


SpooledTemporaryFile.seekable = _seekable