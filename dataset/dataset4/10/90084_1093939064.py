from functools import singledispatchmethod

class Test:
    def __init__(self):
        ...

    @singledispatchmethod
    def get(self, filters):
        return 'Not Implemented!'

    @get.register
    def _(self, filters: dict):
        for k, v in filters.items():
            print(k, ' => ' ,  v)

    @get.register
    def _(self, filters: list):
        for f in filters:
            print(f)

if __name__ == '__main__':
    t = Test()
    t.get({'a': 'A'})
    t.get(['a'])
    t.get(filters={'a': 'A'})