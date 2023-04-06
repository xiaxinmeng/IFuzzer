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

def test_with_error_free_file():
    """Should not display anything if python file is correctly indented."""
    with test_tabnanny.TemporaryPyFile(test_tabnanny.SOURCE_CODES['error_free']) as file_path:
        TestCommandLine.validate_cmd(file_path)

TestCommandLine = test_tabnanny.TestCommandLine()
test_with_error_free_file()
