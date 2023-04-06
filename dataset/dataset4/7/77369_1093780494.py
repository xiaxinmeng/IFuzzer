from typing import TypeVar, Generic
from types import new_class
MyTypeVar = TypeVar("MyTypeVar")
MyParent = new_class("MyParent", (Generic[MyTypeVar],), {})
c = type('MyChild', (MyParent[int],), {})  # error in 3.8