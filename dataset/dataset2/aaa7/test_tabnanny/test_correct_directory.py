from unittest import TestCase, mock
from unittest import mock
import errno
import os
import tabnanny
import tokenize
import tempfile
import textwrap
from test.support import captured_stderr, captured_stdout, script_helper, findfile
from test.support.os_helper import unlink
import test_tabnanny

def test_correct_directory():
    """Directory which contains few error free python source code files."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        with test_tabnanny.TemporaryPyFile(test_tabnanny.SOURCE_CODES['error_free'], directory=tmp_dir):
            TestCheck.verify_tabnanny_check(tmp_dir)

TestCheck = test_tabnanny.TestCheck()
test_correct_directory()
