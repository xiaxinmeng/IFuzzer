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

def test_run_module_bug1764407():
    p = spawn_python('-i', '-m', 'timeit', '-n', '1')
    p.stdin.write(b'Timer\n')
    p.stdin.write(b'exit()\n')
    data = kill_python(p)
    CmdLineTest.assertTrue(data.find(b'1 loop') != -1)
    CmdLineTest.assertTrue(data.find(b'__main__.Timer') != -1)

CmdLineTest = test_cmd_line.CmdLineTest()
test_run_module_bug1764407()
