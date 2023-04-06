import pickle

data = {'a' : [1, 2, 3], 'b': 5}
ps = pickle.dumps(data)
newdata = pickle.loads(ps)
print(newdata)