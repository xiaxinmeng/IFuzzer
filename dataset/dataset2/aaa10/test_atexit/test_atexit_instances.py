import atexit
import os
import sys
import textwrap
import unittest
from test import support
from test.support import script_helper
import test_atexit

def test_atexit_instances():
    code = textwrap.dedent('\n            import sys\n            import atexit as atexit1\n            del sys.modules[\'atexit\']\n            import atexit as atexit2\n            del sys.modules[\'atexit\']\n\n            assert atexit2 is not atexit1\n\n            atexit1.register(print, "atexit1")\n            atexit2.register(print, "atexit2")\n        ')
    res = script_helper.assert_python_ok('-c', code)
    FunctionalTest.assertEqual(res.out.decode().splitlines(), ['atexit2', 'atexit1'])
    FunctionalTest.assertFalse(res.err)

FunctionalTest = test_atexit.FunctionalTest()
test_atexit_instances()
