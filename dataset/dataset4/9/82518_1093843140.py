import inspect

class Example:
    def __init__(self, var):
        self._var = var
        print('__init__')

    def foo(self, bar):
        print(bar)
        print('foo')

    @property
    def var(self):
        print('Access property')
        return self._var


if __name__ == '__main__':
    ex = Example('Hello')
    print('--- getmembers from instance ---')
    print(inspect.getmembers(ex))
    print('--- getmembers from class    ---')
    print(inspect.getmembers(Example))