
from unittest import mock
def func():
    print('Original func called')
    return "ORIGINAL"

m = mock.Mock(wraps=func)

def side_effect():
    print('Side effect func called')
    return "SIDE EFFECT"


m.side_effect = side_effect
print(m())
