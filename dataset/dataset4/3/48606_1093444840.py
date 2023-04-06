class Arr:
    def __getitem__(self, i):
        return foo(i)  # your key function
    def __len__(self):
        return 10000000  # your max index value