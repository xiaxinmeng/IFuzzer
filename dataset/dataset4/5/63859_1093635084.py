class Foo:
    def bar(self, func):
        return func

    @staticmethod
    def baz(func):
        return func
	
    @staticmethod
    def quux():
        def dec(func):
            return func
        return dec

# invalid
@Foo().bar
def f(): pass

# valid
@Foo.baz
def f(): pass

# valid
@Foo.quux()
def f(): pass