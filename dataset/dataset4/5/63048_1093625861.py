def run(self, result=None):
    orig_result = result
    if result is None:
        result = self.defaultTestResult()
        startTestRun = getattr(result, 'startTestRun', None)
        if startTestRun is not None:
            startTestRun()
    # ...