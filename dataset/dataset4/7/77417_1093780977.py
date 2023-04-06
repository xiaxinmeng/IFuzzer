from unittest.mock import MagicMock
m = MagicMock()
assert x.__iter__() is x.__iter__.return_value    # <- fails