from typing import _TypedDictMeta

class UserDictMeta(_TypedDictMeta):
    def __instancecheck__(cls, arg: object) -> bool:
        return (
            isinstance(arg, dict) and
            isinstance(arg.get('name'), str) and
            isinstance(arg.get('registered'), bool)
        )


class UserDict(User, metaclass=UserDictMeta):
    ...