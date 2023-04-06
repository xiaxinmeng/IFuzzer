import pickle
import mmap
data = "some data"

with open('my_data.pkl', 'wb') as f:
    pickle.dump(data, f)

with open("my_data.pkl", "r+b") as f_in:
    mm = mmap.mmap(f_in.fileno(), 0)

print(pickle.load(mm))
