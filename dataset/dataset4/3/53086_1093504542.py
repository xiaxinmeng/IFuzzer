from io import StringIO; s = StringIO(); print(repr(s.getvalue()))
print('abc', file=s); print(repr(s.getvalue()))
s.truncate(0); print(repr(s.getvalue()))
print('abc', file=s); print(repr(s.getvalue()))