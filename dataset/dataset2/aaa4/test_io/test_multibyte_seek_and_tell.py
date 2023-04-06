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

def test_multibyte_seek_and_tell():
    f = TextIOWrapperTest.open(os_helper.TESTFN, 'w', encoding='euc_jp')
    f.write('AB\nうえ\n')
    f.close()
    f = TextIOWrapperTest.open(os_helper.TESTFN, 'r', encoding='euc_jp')
    TextIOWrapperTest.assertEqual(f.readline(), 'AB\n')
    p0 = f.tell()
    TextIOWrapperTest.assertEqual(f.readline(), 'うえ\n')
    p1 = f.tell()
    f.seek(p0)
    TextIOWrapperTest.assertEqual(f.readline(), 'うえ\n')
    TextIOWrapperTest.assertEqual(f.tell(), p1)
    f.close()

TextIOWrapperTest = test_io.TextIOWrapperTest()
test_multibyte_seek_and_tell()
