class u(unicode):
   def __getitem__(self, index):
      return u(2*unicode.__getitem__(self, index))