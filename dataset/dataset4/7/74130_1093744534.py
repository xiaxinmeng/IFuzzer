def make_class_closure(__class__):
    '''Makes a one-tuple closure with a cell for the provided class'''
    return (lambda: super).__closure__

class MyList(list):
    def insert(self, index, object):
        super().insert(index, object)

class MyList2(list):
    pass

MyList2.insert = types.FunctionType(MyList.insert.__code__, globals(), closure=make_class_closure(MyList2))