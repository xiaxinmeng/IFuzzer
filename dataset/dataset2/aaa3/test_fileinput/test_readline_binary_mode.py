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

def test_readline_binary_mode():
    with open(TESTFN, 'wb') as f:
        f.write(b'A\nB\r\nC\rD')
    FileInputTests.addCleanup(safe_unlink, TESTFN)
    with FileInput(files=TESTFN, mode='rb') as fi:
        FileInputTests.assertEqual(fi.readline(), b'A\n')
        FileInputTests.assertEqual(fi.readline(), b'B\r\n')
        FileInputTests.assertEqual(fi.readline(), b'C\rD')
        FileInputTests.assertEqual(fi.readline(), b'')
        FileInputTests.assertEqual(fi.readline(), b'')

FileInputTests = test_fileinput.FileInputTests()
test_readline_binary_mode()
