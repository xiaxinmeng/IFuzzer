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

def test_context_manager():
    d = TestNamedTemporaryFile.do_create()
    with d as name:
        TestNamedTemporaryFile.assertTrue(os.path.exists(name))
        TestNamedTemporaryFile.assertEqual(name, d.name)
    TestNamedTemporaryFile.assertFalse(os.path.exists(name))

TestNamedTemporaryFile = test_tempfile.TestNamedTemporaryFile()
test_context_manager()
