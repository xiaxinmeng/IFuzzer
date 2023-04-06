l = None
for n in itertools.count():
    for i in range(100):
        l = [l]
    print(n,i)
    _pickle.Pickler(io.BytesIO(), protocol=-1).dump(l)