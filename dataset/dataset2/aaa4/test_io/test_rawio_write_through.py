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

def test_rawio_write_through():
    raw = TextIOWrapperTest.MockRawIO([b'abc', b'def', b'ghi\njkl\nopq\n'])
    txt = TextIOWrapperTest.TextIOWrapper(raw, encoding='ascii', newline='\n', write_through=True)
    txt.write('1')
    txt.write('23\n4')
    txt.write('5')
    TextIOWrapperTest.assertEqual(b''.join(raw._write_stack), b'123\n45')

TextIOWrapperTest = test_io.TextIOWrapperTest()
test_rawio_write_through()
