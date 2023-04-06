from unittest.mock import MagicMock
x = MagicMock()

print(x.__iter__())
print(x.__iter__.return_value)
print(x.return_value)