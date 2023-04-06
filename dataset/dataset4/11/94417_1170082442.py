In [1]: args = ['foo', '', 'bar', '']

In [2]: list(filter(None, args))
Out[2]: ['foo', 'bar']