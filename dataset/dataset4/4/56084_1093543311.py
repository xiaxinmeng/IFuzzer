import collections, pickle

class Mydict(collections.OrderedDict):
    def __init__(self, *args, name=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name

a = Mydict(name='foo')
b = pickle.loads(pickle.dumps(a))
print(a.name, b.name)