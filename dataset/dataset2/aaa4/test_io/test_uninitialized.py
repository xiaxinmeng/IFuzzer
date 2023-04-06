import abc
import array
import errno
import locale
import os
import pickle
import random
import signal
import sys
import sysconfig
import textwrap
import threading
import time
import unittest
import warnings
import weakref
from collections import deque, UserList
from itertools import cycle, count
from test import support
from test.support.script_helper import assert_python_ok, assert_python_failure, run_python_until_end
from test.support import import_helper
from test.support import os_helper
from test.support import threading_helper
from test.support import warnings_helper
from test.support.os_helper import FakePath
import codecs
import io
import _pyio as pyio
import ctypes
import _testcapi
import test_io

def test_uninitialized():
    t = BufferedReaderTest.TextIOWrapper.__new__(BufferedReaderTest.TextIOWrapper)
    del t
    t = BufferedReaderTest.TextIOWrapper.__new__(BufferedReaderTest.TextIOWrapper)
    BufferedReaderTest.assertRaises(Exception, repr, t)
    BufferedReaderTest.assertRaisesRegex((ValueError, AttributeError), 'uninitialized|has no attribute', t.read, 0)
    t.__init__(BufferedReaderTest.MockRawIO())
    BufferedReaderTest.assertEqual(t.read(0), '')

BufferedReaderTest = test_io.BufferedReaderTest()
test_uninitialized()
