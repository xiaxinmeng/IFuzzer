
from unittest.mock import patch

class Foo:
    def bar(self, x):
        return x

with patch.object(Foo, 'bar', spec=True) as mock_bar:
    f = Foo()
    f.bar(7)

mock_bar.assert_called_once_with(7)

