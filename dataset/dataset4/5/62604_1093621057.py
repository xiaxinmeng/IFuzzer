import dbm

d = dbm.open('spam', 'c')
d['x'] = '1'
print(len(d))