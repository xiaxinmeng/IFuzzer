import select
a = 1
b = id(a)
c = select.kevent(a)
d = select.kevent(b)
assert a == c.ident
assert b == d.ident
assert b & (1<<32) - 1 == d.ident