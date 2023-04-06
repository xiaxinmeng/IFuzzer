def mydump(obj, file, *args, **kwargs):
    return pickle.dump(obj, Writer(file), *args, **kwargs)

def myload(file, *args, **kwargs):
    return pickle.load(Reader(file), *args, **kwargs)