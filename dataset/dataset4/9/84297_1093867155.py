class AlwaysShared:

   opt = DEFAULT

   def __init__(self, attr, optional=None):
       self.attr = attr
       if optional:
           self.opt = optional

class SometimesShared:

   opt = DEFAULT

   def __init__(self, attr, optional=None):
       if optional:
           self.opt = optional
       self.attr = attr