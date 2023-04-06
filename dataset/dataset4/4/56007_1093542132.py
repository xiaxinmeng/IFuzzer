def run(self, result):
    for index, test in enumerate(self._tests):
        if result.shouldStop:
            break
        test(result)