class Foo:
    def __del__(self):
        raise "pum"

a = Foo()