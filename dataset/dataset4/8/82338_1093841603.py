from unittest.mock import mock_open, patch

DEFAULT_MOCK_DATA = "default mock data"
data_dict = {"file1": "data1",
             "file2": "data2"}

def open_side_effect(name):
    return mock_open(read_data=data_dict.get(name, DEFAULT_MOCK_DATA))()

with patch(f"{__name__}.open", side_effect=open_side_effect):
    with open("file1") as file1:
        assert file1.read() == "data1"

        with open("file2") as file2:
            assert file2.read() == "data2"

            with open("file1") as file3:
                assert file3.read(1) == "d"