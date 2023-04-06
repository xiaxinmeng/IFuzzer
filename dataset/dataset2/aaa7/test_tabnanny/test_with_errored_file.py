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

def test_with_errored_file():
    """Should displays error when errored python file is given."""
    with test_tabnanny.TemporaryPyFile(test_tabnanny.SOURCE_CODES['wrong_indented']) as file_path:
        stderr = f'{file_path!r}: Indentation Error: '
        stderr += 'unindent does not match any outer indentation level (<tokenize>, line 3)'
        TestCommandLine.validate_cmd(file_path, stderr=stderr)

TestCommandLine = test_tabnanny.TestCommandLine()
test_with_errored_file()
