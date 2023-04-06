
class LL(Sequence):
    def __len__(self):
        return 3
    def __getitem__(self, i):
        if i >= 10:
            raise IndexError
        return i * 10

assert LL().index(70) == 7
