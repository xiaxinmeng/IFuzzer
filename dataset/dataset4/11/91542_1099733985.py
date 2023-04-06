
In [111]: c
Out[111]: {'x/y': [{'test': 'eval %s', 'view': 'x'}]}

In [112]: mailcap.findmatch(c, "x/y", filename="exit 1", plist='"echo hello"')
hello
Out[112]: ('x', {'test': 'eval %s', 'view': 'x'})
