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
def test__getitem__invalid_key():
    """Tests invoking FileInput.__getitem__() with an index unequal to
           the line number"""
    t = FileInputTests.writeTmp('line1\nline2\n')
    with FileInput(files=[t]) as fi:
        with FileInputTests.assertRaises(RuntimeError) as cm:
            fi[1]
    FileInputTests.assertEqual(cm.exception.args, ('accessing lines out of order',))

FileInputTests = test_fileinput.FileInputTests()
test__getitem__invalid_key()
