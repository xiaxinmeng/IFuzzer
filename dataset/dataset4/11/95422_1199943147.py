
foo = [(1,1),(2,2)]
ndict = dict(foo)
for n, v in enumerate(ndict.items(), 1):
    if n == len(ndict):
        ndict[1] = 9
print(ndict)
