class cached_property:
    def __init__(self, func, attrname=None):
        self.attrname = attrname
        ...

cls.age3 = cached_property(age, 'age3')