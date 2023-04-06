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

@mock.patch('tabnanny.NannyNag')
def test_with_correct_code(TestProcessTokens, MockNannyNag):
    """A python source code without any whitespace related problems."""
    with test_tabnanny.TemporaryPyFile(test_tabnanny.SOURCE_CODES['error_free']) as file_path:
        with open(file_path) as f:
            tabnanny.process_tokens(tokenize.generate_tokens(f.readline))
        TestProcessTokens.assertFalse(MockNannyNag.called)

TestProcessTokens = test_tabnanny.TestProcessTokens()
test_with_correct_code()
