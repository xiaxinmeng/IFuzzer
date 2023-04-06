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

def test_unbuffered_input():
    code = 'import sys; sys.stdout.write(sys.stdin.read(1))'
    p = spawn_python('-u', '-c', code)
    p.stdin.write(b'x')
    p.stdin.flush()
    (data, rc) = test_cmd_line._kill_python_and_exit_code(p)
    CmdLineTest.assertEqual(rc, 0)
    CmdLineTest.assertTrue(data.startswith(b'x'), data)

CmdLineTest = test_cmd_line.CmdLineTest()
test_unbuffered_input()
