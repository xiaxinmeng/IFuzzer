
s = SimpleCookie(); s.load("invalid\x00=cookie;valid=b", ignore_errors=True)
s2 = SimpleCookie(); s2.load("invalid/=cookie;valid=b", ignore_errors=True)
assert s == s2  # Raises AssertionError.
