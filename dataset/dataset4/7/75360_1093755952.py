
from unittest.mock import MagicMock
mock = MagicMock()
mock.a = 'test'
del mock.a
mock.reset_mock()
