def cmp(x, y):
    return y - x
    
sorted(range(1, 10000000), key=cmp_to_key(cmp))