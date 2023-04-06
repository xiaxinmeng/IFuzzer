from unittest import mock
import inspect

m = mock.AsyncMock()
with mock.patch("inspect.isfunction", new=lambda x: True):
    assert inspect.iscoroutinefunction(m)