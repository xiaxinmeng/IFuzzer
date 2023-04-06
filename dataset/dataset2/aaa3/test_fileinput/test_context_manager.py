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

def test_context_manager():
    t1 = FileInputTests.writeTmp('A\nB\nC')
    t2 = FileInputTests.writeTmp('D\nE\nF')
    with FileInput(files=(t1, t2)) as fi:
        lines = list(fi)
    FileInputTests.assertEqual(lines, ['A\n', 'B\n', 'C', 'D\n', 'E\n', 'F'])
    FileInputTests.assertEqual(fi.filelineno(), 3)
    FileInputTests.assertEqual(fi.lineno(), 6)
    FileInputTests.assertEqual(fi._files, ())

FileInputTests = test_fileinput.FileInputTests()
test_context_manager()
