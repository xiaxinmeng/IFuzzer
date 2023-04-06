import warnings

class BadLoader:
    def get_source(self, fullname):
        class BadSource:
            def splitlines(self):
                return 42
        return BadSource()