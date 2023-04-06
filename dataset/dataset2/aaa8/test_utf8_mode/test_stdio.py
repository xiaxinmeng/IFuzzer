import locale
import subprocess
import sys
import textwrap
import unittest
from test import support
from test.support.script_helper import assert_python_ok, assert_python_failure
from test.support import os_helper
import test_utf8_mode

def test_stdio():
    code = textwrap.dedent('\n            import sys\n            print(f"stdin: {sys.stdin.encoding}/{sys.stdin.errors}")\n            print(f"stdout: {sys.stdout.encoding}/{sys.stdout.errors}")\n            print(f"stderr: {sys.stderr.encoding}/{sys.stderr.errors}")\n        ')
    out = UTF8ModeTests.get_output('-X', 'utf8', '-c', code, PYTHONIOENCODING='')
    UTF8ModeTests.assertEqual(out.splitlines(), ['stdin: utf-8/surrogateescape', 'stdout: utf-8/surrogateescape', 'stderr: utf-8/backslashreplace'])
    out = UTF8ModeTests.get_output('-X', 'utf8', '-c', code, PYTHONIOENCODING='latin1')
    UTF8ModeTests.assertEqual(out.splitlines(), ['stdin: iso8859-1/strict', 'stdout: iso8859-1/strict', 'stderr: iso8859-1/backslashreplace'])
    out = UTF8ModeTests.get_output('-X', 'utf8', '-c', code, PYTHONIOENCODING=':namereplace')
    UTF8ModeTests.assertEqual(out.splitlines(), ['stdin: utf-8/namereplace', 'stdout: utf-8/namereplace', 'stderr: utf-8/backslashreplace'])

UTF8ModeTests = test_utf8_mode.UTF8ModeTests()
test_stdio()
