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

def test_reconfigure_write():
    raw = TextIOWrapperTest.BytesIO()
    txt = TextIOWrapperTest.TextIOWrapper(raw, encoding='latin1', newline='\n')
    txt.write('abcé\n')
    txt.reconfigure(encoding='utf-8')
    TextIOWrapperTest.assertEqual(raw.getvalue(), b'abc\xe9\n')
    txt.write('déf\n')
    txt.flush()
    TextIOWrapperTest.assertEqual(raw.getvalue(), b'abc\xe9\nd\xc3\xa9f\n')
    raw = TextIOWrapperTest.BytesIO()
    txt = TextIOWrapperTest.TextIOWrapper(raw, encoding='ascii', newline='\n')
    txt.write('abc\n')
    txt.reconfigure(encoding='utf-8-sig')
    txt.write('déf\n')
    txt.flush()
    TextIOWrapperTest.assertEqual(raw.getvalue(), b'abc\nd\xc3\xa9f\n')

TextIOWrapperTest = test_io.TextIOWrapperTest()
test_reconfigure_write()
