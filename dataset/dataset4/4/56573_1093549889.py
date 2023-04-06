from multiprocessing.managers import BaseManager

class MathsClass(object):
    def foo(self):
        return 42

class MyManager(BaseManager):
    pass

MyManager.register('Maths', MathsClass)

if __name__ == '__main__':
    manager = MyManager()
    manager.start()
    maths = manager.Maths()
    maths.foo()
    manager.shutdown()
    try:
        maths.foo()
    finally:
        manager.shutdown()