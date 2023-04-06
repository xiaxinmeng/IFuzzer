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

def test_correct_file():
    """A python source code file without any errors."""
    with test_tabnanny.TemporaryPyFile(test_tabnanny.SOURCE_CODES['error_free']) as file_path:
        TestCheck.verify_tabnanny_check(file_path)

TestCheck = test_tabnanny.TestCheck()
test_correct_file()
