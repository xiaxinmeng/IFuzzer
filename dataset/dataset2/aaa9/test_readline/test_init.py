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

@unittest.skipIf(readline._READLINE_VERSION < 1537 and (not is_editline), 'not supported in this library version')
def test_init():
    (rc, stdout, stderr) = assert_python_ok('-c', 'import readline', TERM='xterm-256color')
    TestReadline.assertEqual(stdout, b'')

TestReadline = test_readline.TestReadline()
test_init()
