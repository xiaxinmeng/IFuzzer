class WaitableMock(Mock):

    def __init__(self, *args, **kwargs):
        event_class = kwargs.pop('event_class', threading.Event)
        _safe_super(WaitableMock, self).__init__(*args, **kwargs)
        self.event = event_class()

    def _mock_call(self, *args, **kwargs):
        _safe_super(WaitableMock, self)._mock_call(*args, **kwargs)
        self.event.set()

    def wait_until_called(self, timeout=1):
        return self.event.wait(timeout=timeout)