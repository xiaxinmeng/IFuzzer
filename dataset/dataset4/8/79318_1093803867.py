class C(object):
    @property
    def __class__(self):
        raise AssertionError('fail')