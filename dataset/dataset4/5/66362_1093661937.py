_suite = None

def load_tests(loader, suite, pattern):
    global _suite
    if _suite is None:
        _suite = suite
    return _suite