class Boolean(metaclass=ABCMeta):
    """
    An abstract base class for booleans.
    """
    __slots__ = ()

    @abstractmethod
    def __bool__(self):
        """Return a builtin bool instance. Called for bool(self)."""

    @abstractmethod
    def __and__(self, other):
        """self & other"""

    @abstractmethod
    def __rand__(self, other):
        """other & self"""

    @abstractmethod
    def __xor__(self, other):
        """self ^ other"""

    @abstractmethod
    def __rxor__(self, other):
        """other ^ self"""

    @abstractmethod
    def __or__(self, other):
        """self | other"""

    @abstractmethod
    def __ror__(self, other):
        """other | self"""

    @abstractmethod
    def __invert__(self):
        """~self"""


# register bool and numpy bool_ as virtual subclasses
# so that issubclass(bool, Boolean) = issubclass(np.bool_, Boolean) = True
Boolean.register(bool)