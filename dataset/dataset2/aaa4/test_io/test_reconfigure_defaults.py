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

def test_reconfigure_defaults():
    txt = TextIOWrapperTest.TextIOWrapper(TextIOWrapperTest.BytesIO(), 'ascii', 'replace', '\n')
    txt.reconfigure(encoding=None)
    TextIOWrapperTest.assertEqual(txt.encoding, 'ascii')
    TextIOWrapperTest.assertEqual(txt.errors, 'replace')
    txt.write('LF\n')
    txt.reconfigure(newline='\r\n')
    TextIOWrapperTest.assertEqual(txt.encoding, 'ascii')
    TextIOWrapperTest.assertEqual(txt.errors, 'replace')
    txt.reconfigure(errors='ignore')
    TextIOWrapperTest.assertEqual(txt.encoding, 'ascii')
    TextIOWrapperTest.assertEqual(txt.errors, 'ignore')
    txt.write('CRLF\n')
    txt.reconfigure(encoding='utf-8', newline=None)
    TextIOWrapperTest.assertEqual(txt.errors, 'strict')
    txt.seek(0)
    TextIOWrapperTest.assertEqual(txt.read(), 'LF\nCRLF\n')
    TextIOWrapperTest.assertEqual(txt.detach().getvalue(), b'LF\nCRLF\r\n')

TextIOWrapperTest = test_io.TextIOWrapperTest()
test_reconfigure_defaults()
