from unittest.mock import Mock

m = Mock()
m(1, 2, foo='bar', bar='baz')
m.assert_called_with(2, 3, bar='baz', foo='car')