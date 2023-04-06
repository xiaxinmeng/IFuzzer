import sys
import os
import tempfile
import textwrap
import unittest

import test_pkg

def test_4():
    hier = [('t4.py', "raise RuntimeError('Shouldnt load t4.py')"), ('t4', None), ('t4 __init__.py', ''), ('t4 sub.py', "raise RuntimeError('Shouldnt load sub.py')"), ('t4 sub', None), ('t4 sub __init__.py', ''), ('t4 sub subsub.py', "raise RuntimeError('Shouldnt load subsub.py')"), ('t4 sub subsub', None), ('t4 sub subsub __init__.py', 'spam = 1')]
    TestPkg.mkhier(hier)
    s = '\n            from t4.sub.subsub import *\n            TestPkg.assertEqual(spam, 1)\n            '
    TestPkg.run_code(s)

TestPkg = test_pkg.TestPkg()
TestPkg.setUp()
test_4()
