import tempfile
import errno
import io
import os
import pathlib
import sys
import re
import warnings
import contextlib
import stat
import types
import weakref
from unittest import mock
import unittest
from test import support
from test.support import os_helper
from test.support import script_helper
from test.support import warnings_helper
import test_tempfile
if sys.platform.startswith('openbsd'):
    TEST_FILES = 48
else:
    TEST_FILES = 100
def test_many():
    extant = list(range(TEST_FILES))
    for i in extant:
        extant[i] = TestRandomNameSequence.do_create(pre='aa')

TestRandomNameSequence = test_tempfile.TestRandomNameSequence()
TestRandomNameSequence.setUp()
test_many()
