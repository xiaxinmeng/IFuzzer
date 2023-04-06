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

def test_del___main__():
    filename = os_helper.TESTFN
    CmdLineTest.addCleanup(os_helper.unlink, filename)
    with open(filename, 'w') as script:
        print('import sys', file=script)
        print("del sys.modules['__main__']", file=script)
    assert_python_ok(filename)

CmdLineTest = test_cmd_line.CmdLineTest()
test_del___main__()
