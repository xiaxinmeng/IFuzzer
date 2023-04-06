import pickle, _pickle
a=()
for i in range(1000): a = (a,)
pickle.dumps(a) # or _pickle.dumps(a)