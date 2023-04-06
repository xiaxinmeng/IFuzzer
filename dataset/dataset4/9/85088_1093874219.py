a = ([],)
try:
    b = a[0]
    b += [1]
    a[0] = b
except TypeError:
    assert a != ([1],)  # assertion fails
else:
    assert a == ([1],)