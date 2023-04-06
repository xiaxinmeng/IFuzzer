from unittest.mock import MagicMock


class CustomMock(MagicMock):
    def __init__(self):
        super().__init__(__something__='something')


mock = CustomMock()
MagicMock(mock)