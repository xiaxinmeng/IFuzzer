import sys
import os
import tempfile
import textwrap
import unittest

import test_pkg

def test_5():
    hier = [('t5', None), ('t5 __init__.py', 'import t5.foo'), ('t5 string.py', 'spam = 1'), ('t5 foo.py', 'from . import string; assert string.spam == 1')]
    TestPkg.mkhier(hier)
    import t5
    s = "\n            from t5 import *\n            TestPkg.assertEqual(dir(), ['foo', 'TestPkg', 'string', 't5'])\n            "
    TestPkg.run_code(s)
    import t5
    TestPkg.assertEqual(test_pkg.fixdir(dir(t5)), ['__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'foo', 'string', 't5'])
    TestPkg.assertEqual(test_pkg.fixdir(dir(t5.foo)), ['__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'string'])
    TestPkg.assertEqual(test_pkg.fixdir(dir(t5.string)), ['__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'spam'])

TestPkg = test_pkg.TestPkg()
TestPkg.setUp()
test_5()
