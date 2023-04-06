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

def test_close_on_exception():
    t1 = FileInputTests.writeTmp('')
    try:
        with FileInput(files=t1) as fi:
            raise OSError
    except OSError:
        FileInputTests.assertEqual(fi._files, ())

FileInputTests = test_fileinput.FileInputTests()
test_close_on_exception()
