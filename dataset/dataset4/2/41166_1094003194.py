def __getitem__(self, i):
    return datetime.date(2001, i, 1).strftime(self.format)