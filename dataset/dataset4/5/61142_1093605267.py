class Boom:
    def __dir__(self):
        return ['BOOM']
    def __getattr__(self, name):
        if name =='BOOM':
            return 42
        return super().__getattr(name)

help(Boom)