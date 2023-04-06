
import pickle
import weakref

pickle.dumps(weakref.ref(int))  # TypeError: cannot pickle 'weakref' object
