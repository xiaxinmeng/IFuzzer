import pickle
import io

class P(pickle.Pickler):
    def persistent_id(self, obj):
        if obj is a[0]:
            a.clear()
        return None

a = [[[[]]]]
P(io.BytesIO()).dump(a)