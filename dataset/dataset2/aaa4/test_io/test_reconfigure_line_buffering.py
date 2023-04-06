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

def test_reconfigure_line_buffering():
    r = TextIOWrapperTest.BytesIO()
    b = TextIOWrapperTest.BufferedWriter(r, 1000)
    t = TextIOWrapperTest.TextIOWrapper(b, newline='\n', line_buffering=False)
    t.write('AB\nC')
    TextIOWrapperTest.assertEqual(r.getvalue(), b'')
    t.reconfigure(line_buffering=True)
    TextIOWrapperTest.assertEqual(r.getvalue(), b'AB\nC')
    t.write('DEF\nG')
    TextIOWrapperTest.assertEqual(r.getvalue(), b'AB\nCDEF\nG')
    t.write('H')
    TextIOWrapperTest.assertEqual(r.getvalue(), b'AB\nCDEF\nG')
    t.reconfigure(line_buffering=False)
    TextIOWrapperTest.assertEqual(r.getvalue(), b'AB\nCDEF\nGH')
    t.write('IJ')
    TextIOWrapperTest.assertEqual(r.getvalue(), b'AB\nCDEF\nGH')
    t.reconfigure()
    t.reconfigure(line_buffering=None)
    TextIOWrapperTest.assertEqual(t.line_buffering, False)
    t.reconfigure(line_buffering=True)
    t.reconfigure()
    t.reconfigure(line_buffering=None)
    TextIOWrapperTest.assertEqual(t.line_buffering, True)

TextIOWrapperTest = test_io.TextIOWrapperTest()
test_reconfigure_line_buffering()
