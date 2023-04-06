a = {0: 0}

for i in a:
    del a[i]
    a[i+1] = 0
    print(i)