
from multiprocessing.managers import BaseManager

class FooBar(object):
    def m(self):
        self._raise()
    def _raise(self):
        raise ValueError

class MyManager(BaseManager):
    pass

MyManager.register('Foo', callable=FooBar)
manager = MyManager()
manager.start()
manager.Foo()._callmethod('m')
manager.shutdown()
