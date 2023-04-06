@abc.update_abstractmethods
@functools.total_ordering
class MyClass(SomeAbstractBaseClass):
    def __lt__(self, other):
        whatever