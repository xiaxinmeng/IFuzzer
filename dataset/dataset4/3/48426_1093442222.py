class C(object):
    def __reduce__(self):
        return C, (), None, None, [] # 5th item is not an iterator
class D(object):
    def __reduce__(self):
        return D, (), None, [], None # 4th item is not an iterator

import sys
if sys.version_info[0] == 3:
    import pickle
else:
    import cPickle as pickle
pickle.dumps(C()) # crash
pickle.dumps(D()) # crash