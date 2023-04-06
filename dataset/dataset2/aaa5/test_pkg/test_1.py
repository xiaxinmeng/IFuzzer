import sys
import os
import tempfile
import textwrap
import unittest



import test_pkg

def test_1():
    hier = [('t1', None), ('t1 __init__.py', '')]
    TestPkg.mkhier(hier)
    import t1

TestPkg = test_pkg.TestPkg()
TestPkg.setUp()
test_1()
