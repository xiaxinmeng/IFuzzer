import collections.abc

class Seq(collections.abc.Sequence):
    def __getitem__(self, i):
        if i >= len(self):
            raise IndexError
        return i
    def __len__(self):
        return 42