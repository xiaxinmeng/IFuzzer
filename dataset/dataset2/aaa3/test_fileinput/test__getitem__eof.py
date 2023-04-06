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

@warnings_helper.ignore_warnings(category=DeprecationWarning)
def test__getitem__eof():
    """Tests invoking FileInput.__getitem__() with the line number but at
           end-of-input"""
    t = FileInputTests.writeTmp('')
    with FileInput(files=[t]) as fi:
        with FileInputTests.assertRaises(IndexError) as cm:
            fi[0]
    FileInputTests.assertEqual(cm.exception.args, ('end of input reached',))

FileInputTests = test_fileinput.FileInputTests()
test__getitem__eof()
