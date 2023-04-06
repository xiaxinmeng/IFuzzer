import os
import sys
import re
import fileinput
import collections
import builtins
import tempfile
import unittest

import gzip
from io import BytesIO, StringIO
from fileinput import FileInput, hook_encoded
from pathlib import Path
from test.support import verbose
from test.support.os_helper import TESTFN
from test.support.os_helper import unlink as safe_unlink
from test.support import os_helper
from test.support import warnings_helper
from test import support
from unittest import mock
import test_fileinput

def test_readline_os_chmod_raises_OSError():
    """Tests invoking FileInput.readline() when os.chmod() raises OSError.
           This exception should be silently discarded."""
    os_chmod_orig = os.chmod
    os_chmod_replacement = test_fileinput.UnconditionallyRaise(OSError)
    try:
        t = FileInputTests.writeTmp('\n')
        with FileInput(files=[t], inplace=True) as fi:
            os.chmod = os_chmod_replacement
            fi.readline()
    finally:
        os.chmod = os_chmod_orig
    FileInputTests.assertTrue(os_chmod_replacement.invoked, 'os.fstat() was not invoked')

FileInputTests = test_fileinput.FileInputTests()
test_readline_os_chmod_raises_OSError()
