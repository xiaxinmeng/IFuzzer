o = object()
for x in range(1000000):
    o = o.__dir__
    print(x, id(o.__dir__))
