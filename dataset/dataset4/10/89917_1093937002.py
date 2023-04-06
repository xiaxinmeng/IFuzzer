# cat test.py
from unittest import mock

class Foo:
    @property
    def bar(self) -> str:
        raise Exception('xxx')

m = mock.MagicMock(spec=Foo())