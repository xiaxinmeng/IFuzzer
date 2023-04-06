def patch(self, *args, **kwargs):
    # lazy import
    from unittest.mock import patch
    p = patch(*args, **kwargs)
    result = p.start()
    self.addCleanup(p.stop)
    return result