import mock

mocked_open = mock.mock_open(read_data='one\n')
f1 = mocked_open('a-name')
line1 = f1.__next__()