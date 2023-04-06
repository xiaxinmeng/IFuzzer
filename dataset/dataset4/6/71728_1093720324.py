class MyStr(str):
    def __repr__(self):
        return 'MyStr(%s)' % str.__repr__(self)