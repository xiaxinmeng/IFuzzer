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

def test_bad_mode():
    dir = tempfile.mkdtemp()
    TestNamedTemporaryFile.addCleanup(os_helper.rmtree, dir)
    with TestNamedTemporaryFile.assertRaises(ValueError):
        tempfile.NamedTemporaryFile(mode='wr', dir=dir)
    with TestNamedTemporaryFile.assertRaises(TypeError):
        tempfile.NamedTemporaryFile(mode=2, dir=dir)
    TestNamedTemporaryFile.assertEqual(os.listdir(dir), [])

TestNamedTemporaryFile = test_tempfile.TestNamedTemporaryFile()
test_bad_mode()
