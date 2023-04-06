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

def test_verbose_mode():
    """Should display more error information if verbose mode is on."""
    with test_tabnanny.TemporaryPyFile(test_tabnanny.SOURCE_CODES['nannynag_errored']) as path:
        stdout = textwrap.dedent('offending line: \'\\tprint("world")\\n\'').strip()
        TestCommandLine.validate_cmd('-v', path, stdout=stdout, partial=True)

TestCommandLine = test_tabnanny.TestCommandLine()
test_verbose_mode()
