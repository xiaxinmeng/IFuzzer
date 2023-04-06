def bar(a: int):
    pass

# /tmp/bar.py
from unittest import mock

import foo

with mock.patch.object(foo, 'bar', autospec=True) as mocked_attribute:
    assert mocked_attribute.__module__ == 'foo'