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

def test_sys_ignores_cleaning_up_user_data():
    code = "if 1:\n            import struct, sys\n\n            class C:\n                def __init__(SysModuleTest):\n                    SysModuleTest.pack = struct.pack\n                def __del__(SysModuleTest):\n                    SysModuleTest.pack('I', -42)\n\n            sys.x = C()\n            "
    (rc, stdout, stderr) = assert_python_ok('-c', code)
    SysModuleTest.assertEqual(rc, 0)
    SysModuleTest.assertEqual(stdout.rstrip(), b'')
    SysModuleTest.assertEqual(stderr.rstrip(), b'')

SysModuleTest = test_sys.SysModuleTest()
test_sys_ignores_cleaning_up_user_data()