class Seq (object):
    def __len__(self):
        return 5

    def __getitem__(self, idx):
        if idx > len(self):
            raise IndexError(idx)
        return idx * 2


i = iter(Seq())