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

def test_context_manager_during_rollover():
    with tempfile.SpooledTemporaryFile(max_size=1) as f:
        TestSpooledTemporaryFile.assertFalse(f._rolled)
        f.write(b'abc\n')
        f.flush()
        TestSpooledTemporaryFile.assertTrue(f._rolled)
        TestSpooledTemporaryFile.assertFalse(f.closed)
    TestSpooledTemporaryFile.assertTrue(f.closed)

    def use_closed():
        with f:
            pass
    TestSpooledTemporaryFile.assertRaises(ValueError, use_closed)

TestSpooledTemporaryFile = test_tempfile.TestSpooledTemporaryFile()
test_context_manager_during_rollover()
