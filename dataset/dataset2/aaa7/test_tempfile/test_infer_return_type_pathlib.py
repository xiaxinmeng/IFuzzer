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

def test_infer_return_type_pathlib():
    TestLowLevelInternals.assertIs(str, tempfile._infer_return_type(pathlib.Path('/')))

TestLowLevelInternals = test_tempfile.TestLowLevelInternals()
test_infer_return_type_pathlib()
