def fastdump(obj, file):
    p = pickle.Pickler(file)
    p.fast = True
    p.dump(obj)