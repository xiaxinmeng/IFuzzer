from unittest.mock import *

m = Mock()
m(1,2)
m.call_args
print("1 ", m.call_args == call(1,2))
print("2 ", m.call_args != call(1,2))