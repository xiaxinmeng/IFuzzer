import itertools
import io
import _pickle

# extracted from 'def test_cpickle' and condensed:
l = None
for n in itertools.count():
    try:
        raise KeyError
    except KeyError:
        for i in range(100):
            l = [l]
        print(n,i)
    _pickle.Pickler(io.BytesIO(), protocol=-1).dump(l)