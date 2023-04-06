@functools.total_ordering
class MyAbstractClass(abc.ABC):
    @abc.abstractmethod
    def __lt__(self, other):
        return NotImplemented