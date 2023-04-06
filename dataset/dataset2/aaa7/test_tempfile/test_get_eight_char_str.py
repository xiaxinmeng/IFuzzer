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

def test_get_eight_char_str():
    s = next(TestRandomNameSequence.r)
    TestRandomNameSequence.nameCheck(s, '', '', '')

TestRandomNameSequence = test_tempfile.TestRandomNameSequence()
TestRandomNameSequence.setUp()
test_get_eight_char_str()
