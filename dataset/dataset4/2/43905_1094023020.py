dct = {}
for i,(k,v) in enumerate(lst):
    dct.setdefault(k, []).append(i)