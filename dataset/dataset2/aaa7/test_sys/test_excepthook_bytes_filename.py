import builtins
import codecs
import gc
import locale
import operator
import os
import struct
import subprocess
import sys
import sysconfig
import test.support
from test import support
from test.support import os_helper
from test.support.script_helper import assert_python_ok, assert_python_failure
from test.support import threading_helper
import textwrap
import unittest
import warnings
from _testinternalcapi import get_recursion_depth
import threading
import traceback
import threading
import traceback
from test.support.script_helper import assert_python_ok
import _testcapi
import _testcapi
import types
import _testinternalcapi
import datetime
import collections
import codecs, encodings.iso8859_3
import inspect
import re
import weakref
from collections import OrderedDict
import _ast
import test_sys

def test_excepthook_bytes_filename():
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', BytesWarning)
        try:
            raise SyntaxError('msg', (b'bytes_filename', 123, 0, 'text'))
        except SyntaxError as exc:
            with support.captured_stderr() as err:
                sys.__excepthook__(*sys.exc_info())
    err = err.getvalue()
    ExceptHookTest.assertIn('  File "b\'bytes_filename\'", line 123\n', err)
    ExceptHookTest.assertIn('    text\n', err)
    ExceptHookTest.assertTrue(err.endswith('SyntaxError: msg\n'))

ExceptHookTest = test_sys.ExceptHookTest()
test_excepthook_bytes_filename()
