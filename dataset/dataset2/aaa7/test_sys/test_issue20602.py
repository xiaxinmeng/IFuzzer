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

def test_issue20602():
    code = 'if 1:\n            import sys\n            class A:\n                def __del__(SysModuleTest, sys=sys):\n                    print(sys.flags)\n                    print(sys.float_info)\n            a = A()\n            '
    (rc, out, err) = assert_python_ok('-c', code)
    out = out.splitlines()
    SysModuleTest.assertIn(b'sys.flags', out[0])
    SysModuleTest.assertIn(b'sys.float_info', out[1])

SysModuleTest = test_sys.SysModuleTest()
test_issue20602()
