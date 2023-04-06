def cmp(x, y):
    x = int(x)
    y = int(y)
    return (x > y) - (y > x)
    
sorted([str(i) for i in reversed(range(1, 2000000))], key=cmp_to_key(cmp))