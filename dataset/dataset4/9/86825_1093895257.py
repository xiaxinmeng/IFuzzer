import platform
import pickle

pack = {
    'uname_result': platform.uname()
}

with open('test.pickle', 'wb') as f:
    pickle.dump(pack, f, protocol=pickle.HIGHEST_PROTOCOL)

with open('test.pickle', 'rb') as f:
    data = pickle.load(f)
