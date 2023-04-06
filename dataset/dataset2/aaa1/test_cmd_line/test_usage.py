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

def test_usage():
    (rc, out, err) = assert_python_ok('-h')
    lines = out.splitlines()
    CmdLineTest.assertIn(b'usage', lines[0])
    b''.join(lines[1:]).decode('ascii')

CmdLineTest = test_cmd_line.CmdLineTest()
test_usage()
