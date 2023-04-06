import atexit
import os
import sys
import textwrap
import unittest
from test import support
from test.support import script_helper
import test_atexit

def test_callbacks_leak_refcycle():
    n = atexit._ncallbacks()
    code = textwrap.dedent('\n            import atexit\n            def f():\n                pass\n            atexit.register(f)\n            atexit.__atexit = atexit\n        ')
    ret = support.run_in_subinterp(code)
    SubinterpreterTest.assertEqual(ret, 0)
    SubinterpreterTest.assertEqual(atexit._ncallbacks(), n)

SubinterpreterTest = test_atexit.SubinterpreterTest()
test_callbacks_leak_refcycle()
