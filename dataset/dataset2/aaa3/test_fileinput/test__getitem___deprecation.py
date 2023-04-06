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

def test__getitem___deprecation():
    t = FileInputTests.writeTmp('line1\nline2\n')
    with FileInputTests.assertWarnsRegex(DeprecationWarning, 'Use iterator protocol instead'):
        with FileInput(files=[t]) as fi:
            FileInputTests.assertEqual(fi[0], 'line1\n')

FileInputTests = test_fileinput.FileInputTests()
test__getitem___deprecation()
