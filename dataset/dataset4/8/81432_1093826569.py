from unittest import mock

mock_obj = mock.MagicMock()
mock_obj.mock_func = mock.MagicMock(spec=lambda x: x)

with mock.patch.object(mock_obj, "mock_func") as nested:
    print(type(nested))