class MultilineStringComment:

    def foo(self):
        pass

class NestedClass:
    a = '''
    class Spam:
        ...
    '''

class Nested:

    class Spam:
        pass

print(inspect.getsource(MultilineStringVariable))
print(inspect.getsource(MultilineStringComment))
print(inspect.getsource(Nested.Spam))