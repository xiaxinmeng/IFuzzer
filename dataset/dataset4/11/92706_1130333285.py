
class DateTime(datetime.datetime):
    """Modification of Python's datetime.datetime to produce an error in situations where the result doesn't make sense
    See: https://github.com/python/cpython/issues/92706
    """
    def __eq__(self, other):
        raise NotImplementedError('BUG IN PYTHON: if you compare two datetime objects, eg x == b, it sometimes gives '
                                  'the wrong answer. A workaround is to compare x.timestamp() == b.timestamp().')

    # do same for __ne__, __gt__, __ge__, __lt__, __le__
