s = set(range(100))
s.clear()
s.update(range(100))
si = iter(s)
s.clear()
a = list(range(100))
s.update(range(100))
list(si)