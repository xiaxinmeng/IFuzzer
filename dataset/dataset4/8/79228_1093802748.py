from unittest import mock

m = mock.Mock()
m(1, 3)
m("Test", data=[42])