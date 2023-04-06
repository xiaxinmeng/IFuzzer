import string
assert len(set(string.hexdigits)) == 22
for c in string.hexdigits:
    assert '0' <= c <= '9' or 'a' <= c <= 'f' or 'A' <= c <= 'F'