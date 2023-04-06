class Foo:
    def __init__(self, data):
        self._bar = data
    
    @property
    def bar(self):
        print('--BAR--')
        return self._bar

inspect.getmembers(Foo('test'), inspect.isdatadescriptor)