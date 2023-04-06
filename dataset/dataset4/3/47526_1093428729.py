import collections.abc

class Multimap(collections.abc.Mapping):
    def __init__(self):
        self.data = collections.defaultdict(list)

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key].append(value)

    def __iter__(self):
        yield from self.data

    def items(self):
        for k in list(self.data.keys()):
            for v in list(self.data[k]):
                yield (k,v)

    def __len__(self):
        return sum([len(v) for v in self.data.values()])

mm = Multimap()
mm['1'] = 'a'
mm['1'] = 'aa'
mm['1'] = 'aaa'
mm['2'] = 'b'
mm['3'] = 'c'
mm['3'] = 'cc'
print(f'len = {len(mm)}')
print(f'mm.items() = {list(mm.items())}')