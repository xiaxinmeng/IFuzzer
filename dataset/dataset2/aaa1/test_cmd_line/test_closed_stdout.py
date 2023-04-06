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

def test_closed_stdout():
    code = 'import sys; sys.stdout.close()'
    (rc, out, err) = assert_python_ok('-c', code)
    CmdLineTest.assertEqual(b'', err)

CmdLineTest = test_cmd_line.CmdLineTest()
test_closed_stdout()
