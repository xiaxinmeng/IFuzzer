import _functools

from struct import pack

def test(*args):
	pass

p = _functools.partial(test)
p.__setstate__((test, ["A"]*0x500, None, None))
p()
