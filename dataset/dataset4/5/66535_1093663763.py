from enum import EnumMeta, Enum
from types import DynamicClassAttribute


class _MultiMeta(EnumMeta):
    def __init__(enum_class, cls, bases, classdict):
        # make sure we only have tuple values, not single values
        for member in enum_class.__members__.values():
            if not isinstance(member._value_, tuple):
                raise ValueError('{!r}, should be tuple'.format(member._value_))

    def __call__(cls, suit):
        for member in cls:
            if suit in member._value_:
                return member
        return super().__call__(suit)


class MultiValueEnum(Enum, metaclass=_MultiMeta):
    @DynamicClassAttribute
    def value(self):
        """The value of the Enum member."""
        return self._value_[0]

class IncorrectAliasBehavior(MultiValueEnum):
    first = 1, 2, 3
    second = 4, 5, 6
    alias_to_first = 1, 2, 3