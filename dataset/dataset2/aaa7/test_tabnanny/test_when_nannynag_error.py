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

def test_when_nannynag_error():
    """A python source code file eligible for raising `tabnanny.NannyNag`."""
    with test_tabnanny.TemporaryPyFile(test_tabnanny.SOURCE_CODES['nannynag_errored']) as file_path:
        out = f'{file_path} 3 \'\\tprint("world")\\n\'\n'
        TestCheck.verify_tabnanny_check(file_path, out=out)

TestCheck = test_tabnanny.TestCheck()
test_when_nannynag_error()
