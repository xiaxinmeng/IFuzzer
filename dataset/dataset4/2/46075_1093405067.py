class MetaNode(type):
    def __init__(cls, name, bases, cdict):
        cdict['z'] = name
        type.__init__(name, bases, cdict)
class Node(object):
    __metaclass__ = MetaNode