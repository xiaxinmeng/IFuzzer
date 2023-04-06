class Tuple(tuple):
    def __getitem__(self, index):
        return 9

a = Tuple([1, 2, 3])
print(a[0])