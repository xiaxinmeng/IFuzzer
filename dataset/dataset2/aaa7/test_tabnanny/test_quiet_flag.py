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

def test_quiet_flag():
    """Should display less when quite mode is on."""
    with test_tabnanny.TemporaryPyFile(test_tabnanny.SOURCE_CODES['nannynag_errored']) as file_path:
        stdout = f'{file_path}\n'
        TestCommandLine.validate_cmd('-q', file_path, stdout=stdout)

TestCommandLine = test_tabnanny.TestCommandLine()
test_quiet_flag()
