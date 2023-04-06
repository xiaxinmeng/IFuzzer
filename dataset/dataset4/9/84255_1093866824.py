import pickle

fname = '/path/to/file.pickle'

with open(fname, 'rb') as f:
    object = pickle.load(f)