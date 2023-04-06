class Foo:
    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError
        if index >= 3:
            raise IndexError
        return index

    def __len__(self):
        return 3