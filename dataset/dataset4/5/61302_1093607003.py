def rotate(od, n):
    for i in range(n):
        k, v = od.popitem(False)
        od[k] = v