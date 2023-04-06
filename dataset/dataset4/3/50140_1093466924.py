class MyProp(property):
    pass

class Foo(object):
    @property
    def bar(self):
        '''Get a bar.'''

    @MyProp
    def baz(self):
        '''Get a baz.'''