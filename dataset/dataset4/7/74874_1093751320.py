class Resolver(object):
    def __getitem__(self, name):
        if name == "test":
            return 0.5
        else:
            raise KeyError

resolvers = (Resolver(), )
pd.eval("test", resolvers=resolvers)