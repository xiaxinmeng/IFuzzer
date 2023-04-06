import pickle
import pickletools

class A:
    pass

data = pickle.dumps(A)
pickletools.dis(data)