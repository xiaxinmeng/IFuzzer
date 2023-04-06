import inspect

class MetaBoom(type):
    def __dir__(cls):
        return ['__class__', '__module__', '__name__', 'BOOM']
    def __getattr__(self, name):
        if name =='BOOM':
            return 42
        return super().__getattr(name)
    def test(self):
        print('testing...')

class Boom(metaclass=MetaBoom):
    pass

help(Boom())