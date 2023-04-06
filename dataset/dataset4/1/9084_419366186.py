
try:
    from _testcapi import bad_get
except ImportError:
    def bad_get(self, obj, cls):
        cls()
        return repr(self)
