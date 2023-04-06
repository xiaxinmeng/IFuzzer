class MetaNode(type):
   def __new__(cls, name, bases, cdict):
       cdict['z'] = name
       return type.__new__(cls, name, bases, cdict)

class Node(object):
   __metaclass__ = MetaNode