import os
import subprocess
import sys
import tempfile
import textwrap
import unittest
from test import support
from test.support import os_helper
from test.support.script_helper import spawn_python, kill_python, assert_python_ok, assert_python_failure, interpreter_requires_environment
import _testcapi
import faulthandler
import test_cmd_line

def test_stdout_flush_at_shutdown():
    code = "if 1:\n            import os, sys, test.support\n            test.support.SuppressCrashReport().__enter__()\n            sys.stdout.write('x')\n            os.close(sys.stdout.fileno())"
    (rc, out, err) = assert_python_failure('-c', code)
    CmdLineTest.assertEqual(b'', out)
    CmdLineTest.assertEqual(120, rc)
    CmdLineTest.assertRegex(err.decode('ascii', 'ignore'), 'Exception ignored in.*\nOSError: .*')

CmdLineTest = test_cmd_line.CmdLineTest()
test_stdout_flush_at_shutdown()
