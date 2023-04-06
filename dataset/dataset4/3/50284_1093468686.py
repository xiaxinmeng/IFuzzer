def __reversed__(self):
   for i in reversed(range(self.__len__)):
      yield self.__getitem__(i)