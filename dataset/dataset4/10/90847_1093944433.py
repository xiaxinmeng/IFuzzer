
from types import FunctionType
a = (x for x in [1])
list(FunctionType(a.gi_code, {})(0))
