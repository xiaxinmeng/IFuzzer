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

def test_command_usage():
    """Should display usage on no arguments."""
    path = findfile('tabnanny.py')
    stderr = f'Usage: {path} [-v] file_or_directory ...'
    TestCommandLine.validate_cmd(stderr=stderr)

TestCommandLine = test_tabnanny.TestCommandLine()
test_command_usage()
