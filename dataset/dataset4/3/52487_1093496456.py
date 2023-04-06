a = 'x' * 20000
# create a copy with a different memory address
b = a[0:] + a[1:]
assert (a == b) and (a is not b)
data = a, b