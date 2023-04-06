
from unittest.mock import MagicMock

m = MagicMock(a=MagicMock())
m.a.return_value = 1
m.reset_mock(return_value=True)
print(m.a())
