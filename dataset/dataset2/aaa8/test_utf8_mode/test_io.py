import locale
import subprocess
import sys
import textwrap
import unittest
from test import support
from test.support.script_helper import assert_python_ok, assert_python_failure
from test.support import os_helper
import test_utf8_mode

def test_io():
    code = textwrap.dedent('\n            import sys\n            filename = sys.argv[1]\n            with open(filename) as fp:\n                print(f"{fp.encoding}/{fp.errors}")\n        ')
    filename = __file__
    out = UTF8ModeTests.get_output('-c', code, filename, PYTHONUTF8='1')
    UTF8ModeTests.assertEqual(out, 'UTF-8/strict')

UTF8ModeTests = test_utf8_mode.UTF8ModeTests()
test_io()
