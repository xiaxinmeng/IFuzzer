
from pydantic import BaseModel
from typing import no_type_check

@no_type_check  # the same with and without this decorator
class MyModel(BaseModel):
    a: int

print(MyModel(a=1))  # ok
print(MyModel(a='1a'))  # ok
# pydantic.error_wrappers.ValidationError: 1 validation error for MyModel
# a: value is not a valid integer (type=type_error.integer)
