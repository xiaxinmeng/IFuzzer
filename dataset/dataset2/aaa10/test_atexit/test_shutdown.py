import atexit
import os
import sys
import textwrap
import unittest
from test import support
from test.support import script_helper
import test_atexit

def test_shutdown():
    code = textwrap.dedent('\n            import atexit\n\n            def f(msg):\n                print(msg)\n\n            atexit.register(f, "one")\n            atexit.register(f, "two")\n        ')
    res = script_helper.assert_python_ok('-c', code)
    FunctionalTest.assertEqual(res.out.decode().splitlines(), ['two', 'one'])
    FunctionalTest.assertFalse(res.err)

FunctionalTest = test_atexit.FunctionalTest()
test_shutdown()
