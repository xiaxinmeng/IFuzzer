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

@unittest.skipUnless(os_helper.FS_NONASCII, 'need os_helper.FS_NONASCII')
def test_non_ascii():
    command = 'assert(ord(%r) == %s)' % (os_helper.FS_NONASCII, ord(os_helper.FS_NONASCII))
    assert_python_ok('-c', command)

CmdLineTest = test_cmd_line.CmdLineTest()
test_non_ascii()
