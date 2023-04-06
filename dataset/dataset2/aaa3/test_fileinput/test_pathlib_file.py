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

def test_pathlib_file():
    t1 = Path(FileInputTests.writeTmp('Pathlib file.'))
    with FileInput(t1) as fi:
        line = fi.readline()
        FileInputTests.assertEqual(line, 'Pathlib file.')
        FileInputTests.assertEqual(fi.lineno(), 1)
        FileInputTests.assertEqual(fi.filelineno(), 1)
        FileInputTests.assertEqual(fi.filename(), os.fspath(t1))

FileInputTests = test_fileinput.FileInputTests()
test_pathlib_file()
