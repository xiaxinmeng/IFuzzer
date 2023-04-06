class E(dict):
    def __getattribute__(self,name):
        try:
            return self[name]
        except KeyError:
            return dict.__getattribute__(self, name)