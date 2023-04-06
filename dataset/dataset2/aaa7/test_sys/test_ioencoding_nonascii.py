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

@unittest.skipUnless(os_helper.FS_NONASCII, 'requires OS support of non-ASCII encodings')
@unittest.skipUnless(sys.getfilesystemencoding() == locale.getpreferredencoding(False), 'requires FS encoding to match locale')
def test_ioencoding_nonascii():
    env = dict(os.environ)
    env['PYTHONIOENCODING'] = ''
    p = subprocess.Popen([sys.executable, '-c', 'print(%a)' % os_helper.FS_NONASCII], stdout=subprocess.PIPE, env=env)
    out = p.communicate()[0].strip()
    SysModuleTest.assertEqual(out, os.fsencode(os_helper.FS_NONASCII))

SysModuleTest = test_sys.SysModuleTest()
test_ioencoding_nonascii()
