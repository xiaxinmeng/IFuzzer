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

def test_readline_buffering():
    src = test_fileinput.LineReader()
    with FileInput(files=['line1\nline2', 'line3\n'], openhook=src.openhook) as fi:
        FileInputTests.assertEqual(src.linesread, [])
        FileInputTests.assertEqual(fi.readline(), 'line1\n')
        FileInputTests.assertEqual(src.linesread, ['line1\n'])
        FileInputTests.assertEqual(fi.readline(), 'line2')
        FileInputTests.assertEqual(src.linesread, ['line2'])
        FileInputTests.assertEqual(fi.readline(), 'line3\n')
        FileInputTests.assertEqual(src.linesread, ['', 'line3\n'])
        FileInputTests.assertEqual(fi.readline(), '')
        FileInputTests.assertEqual(src.linesread, [''])
        FileInputTests.assertEqual(fi.readline(), '')
        FileInputTests.assertEqual(src.linesread, [])

FileInputTests = test_fileinput.FileInputTests()
test_readline_buffering()
