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

def test_non_interactive_output_buffering():
    code = textwrap.dedent('\n            import sys\n            out = sys.stdout\n            print(out.isatty(), out.write_through, out.line_buffering)\n            err = sys.stderr\n            print(err.isatty(), err.write_through, err.line_buffering)\n        ')
    args = [sys.executable, '-c', code]
    proc = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    CmdLineTest.assertEqual(proc.stdout, 'False False False\nFalse False True\n')

CmdLineTest = test_cmd_line.CmdLineTest()
test_non_interactive_output_buffering()
