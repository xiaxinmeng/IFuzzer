import pickle
from import_me import PickleMe

p = PickleMe()

with open('pickled', 'wb') as h:
    pickle.dump(p, h)