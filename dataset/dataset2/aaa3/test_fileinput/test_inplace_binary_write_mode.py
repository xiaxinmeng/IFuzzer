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

def test_inplace_binary_write_mode():
    temp_file = FileInputTests.writeTmp(b'Initial text.', mode='wb')
    with FileInput(temp_file, mode='rb', inplace=True) as fobj:
        line = fobj.readline()
        FileInputTests.assertEqual(line, b'Initial text.')
        sys.stdout.write(b'New line.')
    with open(temp_file, 'rb') as f:
        FileInputTests.assertEqual(f.read(), b'New line.')

FileInputTests = test_fileinput.FileInputTests()
test_inplace_binary_write_mode()
