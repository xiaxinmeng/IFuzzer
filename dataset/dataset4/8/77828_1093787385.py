s = 'this is my string'
for old, new in (('my', 'your'), ('string', 'car')):
    s = s.replace(old, new)
print(s)