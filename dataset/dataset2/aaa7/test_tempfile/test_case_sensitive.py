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

def test_case_sensitive():
    case_sensitive_tempdir = tempfile.mkdtemp('-Temp')
    (_tempdir, tempfile.tempdir) = (tempfile.tempdir, None)
    try:
        with os_helper.EnvironmentVarGuard() as env:
            env['TMPDIR'] = case_sensitive_tempdir
            TestGetTempDir.assertEqual(tempfile.gettempdir(), case_sensitive_tempdir)
    finally:
        tempfile.tempdir = _tempdir
        os_helper.rmdir(case_sensitive_tempdir)

TestGetTempDir = test_tempfile.TestGetTempDir()
test_case_sensitive()
