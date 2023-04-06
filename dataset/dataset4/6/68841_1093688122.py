from unittest import mock
mmock = mock.MagicMock()
mmock.foobar("baz")
mmock.assert_has_calls([])  # No exception raised. Why?mmock.assert_has_calls(['x'])  # Exception raised as expected.