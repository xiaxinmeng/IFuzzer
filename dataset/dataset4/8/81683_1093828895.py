import pickle
pickle.loads(pickle.dumps(1, protocol=pickle.HIGHEST_PROTOCOL), buffers=None)