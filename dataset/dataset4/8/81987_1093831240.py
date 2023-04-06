from typing import Union, List, get_type_hints

ValueList = List['Value']
Value = Union[str, ValueList]

class A:
    a: List[Value]