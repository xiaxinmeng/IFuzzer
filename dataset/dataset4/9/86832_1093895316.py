import inspect

class Foo:
    def spam(self):
        global Bar
        class Bar:
            pass
        print(inspect.getsource(Bar))