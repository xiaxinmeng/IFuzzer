from unittest import mock

m = mock.Mock()
m(1, 2)
m.assert_called_with(2, 3)