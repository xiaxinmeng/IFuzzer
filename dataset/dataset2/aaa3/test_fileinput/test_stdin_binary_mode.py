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

def test_stdin_binary_mode():
    with mock.patch('sys.stdin') as m_stdin:
        m_stdin.buffer = BytesIO(b'spam, bacon, sausage, and spam')
        fi = FileInput(files=['-'], mode='rb')
        lines = list(fi)
        FileInputTests.assertEqual(lines, [b'spam, bacon, sausage, and spam'])

FileInputTests = test_fileinput.FileInputTests()
test_stdin_binary_mode()
