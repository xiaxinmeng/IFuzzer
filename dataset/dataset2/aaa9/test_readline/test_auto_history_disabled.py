from contextlib import ExitStack
from errno import EIO
import locale
import os
import selectors
import subprocess
import sys
import tempfile
import unittest
from test.support import verbose
from test.support.import_helper import import_module
from test.support.os_helper import unlink, temp_dir, TESTFN
from test.support.script_helper import assert_python_ok
import test_readline

def test_auto_history_disabled():
    output = run_pty(TestReadline.auto_history_script.format(False))
    TestReadline.assertIn(b'History length: 0\r\n', output)

TestReadline = test_readline.TestReadline()
test_auto_history_disabled()
