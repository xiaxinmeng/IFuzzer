def mydec(cls):
    return type(cls.__name__, cls.__bases__, dict(cls.__dict__))

@mydec
class MyList(list):
    
    def extend(self, item):
        super(MyList, self).extend(item)
        
    def insert(self, index, object):
        super().insert(index, object)