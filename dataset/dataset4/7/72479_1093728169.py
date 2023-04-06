def itermonthdates(self, year, month):
    for y, m, d in self.itermonthdays3(year, month):
        yield datetime.date(y, m, d)