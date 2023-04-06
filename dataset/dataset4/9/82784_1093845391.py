
class Base:
    def method(self): "some docstring"

def make_subclass():
    class subclass(Base):
        def method(self): return super().method()
    return subclass

subclass = make_subclass()
inspect.getdoc(subclass.method)  # => returns None
