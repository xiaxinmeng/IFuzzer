def testIsinstanceIterNeverCalled(self):
    """Guarantee that __iter__ is never called when isinstance is invoked"""
    class NoIterTuple(tuple):
        def __iter__(self):  # pragma: nocover
            raise NotImplemented("Cannot call __iter__ on this.")

    self.assertTrue(isinstance(1, NoIterTuple((int,))))