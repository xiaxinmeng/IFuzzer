from unittest.mock import MagicMock, call
mm = MagicMock()
mm().foo()['bar']
print(mm.mock_calls)