# Getting the C version of datetime:
import _datetime as cdt

# Getting the pure Python version of datetime:
from test.support import import_fresh_module
pydt = import_fresh_module("datetime", blocked=["_datetime"])