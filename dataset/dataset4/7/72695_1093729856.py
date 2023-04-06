for i in range(25):
    a = {}
    b = {j: j for j in range(i)}
    a.update(b)
    print(i, sys.getsizeof(a))