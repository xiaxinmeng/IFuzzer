class NocaseList(list):

    def __reduce__(self):
        return self.__class__, (), None, iter(self)