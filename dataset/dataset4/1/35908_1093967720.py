import pickle
import random
import string

def genstring(length=100):
    s = [random.choice(string.letters) for x in
range(length)]
    return "".join(s)

def test():
    while 1:
        s = genstring()
        dump = pickle.dumps(s)
        s2 = pickle.loads(dump)
        assert s == s2

test()