def debug(self):
    """Run the test without collecting errors in a TestResult"""
    try:
        self.setUp()
        getattr(self, self._testMethodName)()
        self.tearDown()
    except SkipError:
        pass
    while self._cleanups:
        function, args, kwargs = self._cleanups.pop(-1)
        function(*args, **kwargs)