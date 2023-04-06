a = ([],)
try:
    a[0] += [1]
except TypeError:
    assert a != ([1],)  # assertion fails
else:
    assert a == ([1],)