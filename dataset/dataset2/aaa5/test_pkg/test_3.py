import sys
import os
import tempfile
import textwrap
import unittest

import test_pkg

def test_3():
    hier = [('t3', None), ('t3 __init__.py', ''), ('t3 sub', None), ('t3 sub __init__.py', ''), ('t3 sub subsub', None), ('t3 sub subsub __init__.py', 'spam = 1')]
    TestPkg.mkhier(hier)
    import t3.sub.subsub
    TestPkg.assertEqual(t3.__name__, 't3')
    TestPkg.assertEqual(t3.sub.__name__, 't3.sub')
    TestPkg.assertEqual(t3.sub.subsub.__name__, 't3.sub.subsub')

TestPkg = test_pkg.TestPkg()
TestPkg.setUp()
test_3()
