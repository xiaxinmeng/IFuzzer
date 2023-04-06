class Resolver(UserDict):
    def __init__(self, data={}):
        super(Resolver, self).__init__(data)
        self.data["test"] = None
    
    def __getitem__(self, name):
        if (name == "test"):
            return 0.5
        else:
            super(Resolver, self).__getitem__(name)

resolvers = (Resolver(), )
pd.eval("test", resolvers=resolvers)