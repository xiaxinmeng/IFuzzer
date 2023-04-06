int()
int(base='foo')  # no exception; returns 0
int(x=5)
int(x=5, base=10)  # raises TypeError
int(5.8)  # test truncation towards zero
int(-5.8)  # ditto
int('5.8')  # raises ValueError