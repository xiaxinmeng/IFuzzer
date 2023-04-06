class MyException(Exception):
    def __init__(self, desc, *, item):
        super().__init__()
        self.desc = desc
        self.item = item

    def __getnewargs_ex__(self):
        print('called in {}.__getnewargs_ex__'.format(self.__class__.__name__))
        return (self.desc,), self.__dict__

e = MyException('testing', item='cpu')
s = pickle.dumps(e, protocol=-1)

x = pickle.loads(s)