import contextlib
import importlib
import importlib.machinery
import zipimport
import unittest
import sys
import os
import os.path
import py_compile
import subprocess
import io
import textwrap
from test import support
from test.support import import_helper
from test.support import os_helper
from test.support.script_helper import make_pkg, make_script, make_zip_pkg, make_zip_script, assert_python_ok, assert_python_failure, spawn_python, kill_python
import test_cmd_line_script

def test_nonexisting_script():
    script = 'nonexistingscript.py'
    CmdLineTest.assertFalse(os.path.exists(script))
    proc = spawn_python(script, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, err) = proc.communicate()
    CmdLineTest.assertIn(": can't open file ", err)
    CmdLineTest.assertNotEqual(proc.returncode, 0)

CmdLineTest = test_cmd_line_script.CmdLineTest()
test_nonexisting_script()
