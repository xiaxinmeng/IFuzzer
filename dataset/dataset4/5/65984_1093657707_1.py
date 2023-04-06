class A:
    def __getitem__(self, index):
        return index.start
    def __len__(self):
        return 10