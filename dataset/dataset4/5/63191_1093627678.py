class MyOrderedDict(OrderedDict):
   
    def __getitem__(self, key):
        OrderedDict.__getitem__(self, key)