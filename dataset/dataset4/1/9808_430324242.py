# newtype.py
import typing

# insert the updated NewType class here

UserId = NewType('UserId', int)  # doesn't work as typing.NewType
def name_by_id(user_id: UserId) -> str:
    ...
UserId('user')          # Fails type check
name_by_id(42)          # Fails type check
name_by_id(UserId(42))  # OK
num = UserId(5) + 1     # type: int