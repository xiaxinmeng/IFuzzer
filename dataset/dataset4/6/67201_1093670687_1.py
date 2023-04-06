class RaisingTraceFuncTestCase(unittest.TestCase):
    ...

    def trace(self, frame, event, arg):
        """A trace function that raises an exception in response to a
        specific trace event."""
        if event == self.raiseOnEvent:
            raise ValueError # just something that isn't RuntimeError
        else:
            return self.trace