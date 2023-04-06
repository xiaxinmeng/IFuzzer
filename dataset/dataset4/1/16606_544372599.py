class F:
    @property
    def read(self):
        1/0

import pickle
pickle.load(F())