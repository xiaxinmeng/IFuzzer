import sys
import os
import tempfile
import textwrap
import unittest

import test_pkg

def test_6():
    hier = [('t6', None), ('t6 __init__.py', "__all__ = ['spam', 'ham', 'eggs']"), ('t6 spam.py', ''), ('t6 ham.py', ''), ('t6 eggs.py', '')]
    TestPkg.mkhier(hier)
    import t6
    TestPkg.assertEqual(test_pkg.fixdir(dir(t6)), ['__all__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__'])
    s = "\n            import t6\n            from t6 import *\n            TestPkg.assertEqual(fixdir(dir(t6)),\n                             ['__all__', '__cached__', '__doc__', '__file__',\n                              '__loader__', '__name__', '__package__',\n                              '__path__', '__spec__', 'eggs', 'ham', 'spam'])\n            TestPkg.assertEqual(dir(), ['eggs', 'ham', 'TestPkg', 'spam', 't6'])\n            "
    TestPkg.run_code(s)

TestPkg = test_pkg.TestPkg()
TestPkg.setUp()
test_6()
