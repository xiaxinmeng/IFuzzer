class MyClass(object):

    def __init__(self):
        self.pwn = None

    def __getattribute__(self, name):
        print('MyClass.__getattribute__(self, %r)' % name)
        return getattr('abc', name)

instance = MyClass()
str.strip(instance)