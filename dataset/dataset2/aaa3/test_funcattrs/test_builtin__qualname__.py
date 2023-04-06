import types
import unittest
from collections import UserDict
import time
import test_funcattrs

def test_builtin__qualname__():
    import time
    BuiltinFunctionPropertiesTest.assertEqual(len.__qualname__, 'len')
    BuiltinFunctionPropertiesTest.assertEqual(time.time.__qualname__, 'time')
    BuiltinFunctionPropertiesTest.assertEqual(dict.fromkeys.__qualname__, 'dict.fromkeys')
    BuiltinFunctionPropertiesTest.assertEqual(float.__getformat__.__qualname__, 'float.__getformat__')
    BuiltinFunctionPropertiesTest.assertEqual(str.maketrans.__qualname__, 'str.maketrans')
    BuiltinFunctionPropertiesTest.assertEqual(bytes.maketrans.__qualname__, 'bytes.maketrans')
    BuiltinFunctionPropertiesTest.assertEqual([1, 2, 3].append.__qualname__, 'list.append')
    BuiltinFunctionPropertiesTest.assertEqual({'foo': 'bar'}.pop.__qualname__, 'dict.pop')

BuiltinFunctionPropertiesTest = test_funcattrs.BuiltinFunctionPropertiesTest()
test_builtin__qualname__()
