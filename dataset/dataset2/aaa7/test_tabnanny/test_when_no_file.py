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

def test_when_no_file():
    """A python file which does not exist actually in system."""
    path = 'no_file.py'
    err = f'{path!r}: I/O Error: [Errno {errno.ENOENT}] {os.strerror(errno.ENOENT)}: {path!r}\n'
    TestCheck.verify_tabnanny_check(path, err=err)

TestCheck = test_tabnanny.TestCheck()
test_when_no_file()
