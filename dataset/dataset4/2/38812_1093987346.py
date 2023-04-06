#!/usr/bin/env python
import cPickle as c

class Style:
   def __init__(self):
      self.d = {}

   def __setitem__(self, key, value):
      self.d["d_"+key]=value

   def __getattr__(self, key):
      if key.startswith("d_"):
         return self.d[key]    
      else:
         return self.__dict__[key]

s = Style()
s["A"] = "B"