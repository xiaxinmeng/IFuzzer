def assert_called_once_with(_mock_self, *args, **kwargs):
    self = _mock_self
    if not self.mock_calls.count(call(*args, **kwargs)) == 1:
        msg = ("Expected '%s' to be called once with %r %r. Called %s times."          % (self._mock_name or 'mock', args, kwargs, self.mock_calls.count(call(*args,  **kwargs))))
        raise AssertionError(msg)