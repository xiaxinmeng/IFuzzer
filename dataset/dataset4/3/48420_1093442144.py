class C:
    def __reduce__(self):
        return C, (), None, None, []
class D:
    def __reduce__(self):
        return D, (), None, [], None
import pickle
pickle.dumps(C())
pickle.dumps(D())