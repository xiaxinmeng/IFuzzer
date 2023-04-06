class mdict(dict):
    def __getitem__(self, index):
        print('Getting:', index)
        return super().__getitem__(index)