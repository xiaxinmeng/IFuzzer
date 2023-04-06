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

def test_when_tokenize_tokenerror():
    """A python source code file eligible for raising 'tokenize.TokenError'."""
    with test_tabnanny.TemporaryPyFile(test_tabnanny.SOURCE_CODES['incomplete_expression']) as file_path:
        err = "('EOF in multi-line statement', (7, 0))\n"
        err = f'{file_path!r}: Token Error: {err}'
        TestCheck.verify_tabnanny_check(file_path, err=err)

TestCheck = test_tabnanny.TestCheck()
test_when_tokenize_tokenerror()
