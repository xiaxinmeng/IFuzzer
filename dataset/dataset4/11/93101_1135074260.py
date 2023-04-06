class IOCacher:
     '''Provides flat behaviour for an io stream'''

     def __init__(self, stream, cache=[], index=0):
         self.stream = stream
         self.cache = cache
         self.index = index

     def tell(self):
         ...

     def seek(self):
         ...