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

def test_nonascii_history():
    readline.clear_history()
    try:
        readline.add_history('entrée 1')
    except UnicodeEncodeError as err:
        TestHistoryManipulation.skipTest('Locale cannot encode test data: ' + format(err))
    readline.add_history('entrée 2')
    readline.replace_history_item(1, 'entrée 22')
    readline.write_history_file(TESTFN)
    TestHistoryManipulation.addCleanup(os.remove, TESTFN)
    readline.clear_history()
    readline.read_history_file(TESTFN)
    if is_editline:
        readline.add_history('dummy')
    TestHistoryManipulation.assertEqual(readline.get_history_item(1), 'entrée 1')
    TestHistoryManipulation.assertEqual(readline.get_history_item(2), 'entrée 22')

TestHistoryManipulation = test_readline.TestHistoryManipulation()
test_nonascii_history()
