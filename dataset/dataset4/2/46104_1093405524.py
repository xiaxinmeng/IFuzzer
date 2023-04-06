def CmpToKey(mycmp):
    'Convert a cmp= function into a key= function'
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj
        def __cmp__(self, other):
            return mycmp(self.obj, other.obj)
    return K