
with open("my_data.pkl", "r+b") as f_in:
    mm = mmap.mmap(f_in.fileno(), 0)

print(pickle.loads(memoryview(mm)))
