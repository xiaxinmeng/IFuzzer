gdict = {}
ldict = {}
exec('''
x = 1
def f(): pass''', gdict, ldict)
print(('x' in gdict, 'x' in ldict))