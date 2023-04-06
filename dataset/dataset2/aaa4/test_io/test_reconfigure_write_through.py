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

def test_reconfigure_write_through():
    raw = TextIOWrapperTest.MockRawIO([])
    t = TextIOWrapperTest.TextIOWrapper(raw, encoding='ascii', newline='\n')
    t.write('1')
    t.reconfigure(write_through=True)
    TextIOWrapperTest.assertEqual(t.write_through, True)
    TextIOWrapperTest.assertEqual(b''.join(raw._write_stack), b'1')
    t.write('23')
    TextIOWrapperTest.assertEqual(b''.join(raw._write_stack), b'123')
    t.reconfigure(write_through=False)
    TextIOWrapperTest.assertEqual(t.write_through, False)
    t.write('45')
    t.flush()
    TextIOWrapperTest.assertEqual(b''.join(raw._write_stack), b'12345')
    t.reconfigure()
    t.reconfigure(write_through=None)
    TextIOWrapperTest.assertEqual(t.write_through, False)
    t.reconfigure(write_through=True)
    t.reconfigure()
    t.reconfigure(write_through=None)
    TextIOWrapperTest.assertEqual(t.write_through, True)

TextIOWrapperTest = test_io.TextIOWrapperTest()
test_reconfigure_write_through()