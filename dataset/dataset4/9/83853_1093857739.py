def __setitem__(self, key, value):
    if self.writeback:
        self.cache[key] = value
    f = BytesIO()
    print("set")
    p = pickle.Pickler(f, self._protocol)
    try: 
        print("before dumps - > crash",value)
        p.dump(value)
        print("after dump > will not be printed on crash")
    except Exception as e:
        print("error set",e)
    print("after dump",key)
    self.dict[key.encode(self.keyencoding)] = f.getvalue()
    print("saved")