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

def test_sane_template():
    p = tempfile.gettempprefix()
    TestGetTempPrefix.assertIsInstance(p, str)
    TestGetTempPrefix.assertGreater(len(p), 0)
    pb = tempfile.gettempprefixb()
    TestGetTempPrefix.assertIsInstance(pb, bytes)
    TestGetTempPrefix.assertGreater(len(pb), 0)

TestGetTempPrefix = test_tempfile.TestGetTempPrefix()
test_sane_template()
