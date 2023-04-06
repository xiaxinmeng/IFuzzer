import inspect
import sys
import _testcapi

builtin = _testcapi.docstring_with_signature_with_defaults
spec = inspect.getfullargspec(builtin)
print(type(sys.modules['__builtins__']))