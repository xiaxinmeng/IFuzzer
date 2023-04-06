class DictWriter:
    def __init__(self, f, fieldnames, restval="", extrasaction="raise",
                 dialect="excel", *args, **kwds):
        self._fieldnames = fieldnames    # list of keys for the dict
        self._fieldnames_set = set(self._fieldnames)

    @property
    def fieldnames(self):
        return self._fieldnames

    @fieldnames.setter
    def fieldnames(self, value):
        self._fieldnames = value
        self._fieldnames_set = set(self._fieldnames)


    def _dict_to_list(self, rowdict):
        if self.extrasaction == "raise":
            wrong_fields = rowdict.keys() - self._fieldnames_set
     
    ...