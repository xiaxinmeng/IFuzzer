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

def test_when_wrong_indented():
    """A python source code file eligible for raising `IndentationError`."""
    with test_tabnanny.TemporaryPyFile(test_tabnanny.SOURCE_CODES['wrong_indented']) as file_path:
        err = 'unindent does not match any outer indentation level (<tokenize>, line 3)\n'
        err = f'{file_path!r}: Indentation Error: {err}'
        TestCheck.verify_tabnanny_check(file_path, err=err)

TestCheck = test_tabnanny.TestCheck()
test_when_wrong_indented()
