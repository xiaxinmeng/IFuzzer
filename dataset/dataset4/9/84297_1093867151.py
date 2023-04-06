class C:

   opt = DEFAULT

   def __init__(self, attr, optional=None):
       if optional:
           self.opt = optional
       self.attr = attr