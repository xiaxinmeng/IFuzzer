class Upper(unicode):

    def __getitem__(self, index):
        return unicode.__getitem__(self, index).upper()