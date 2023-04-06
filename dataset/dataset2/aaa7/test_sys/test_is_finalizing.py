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

def test_is_finalizing():
    SysModuleTest.assertIs(sys.is_finalizing(), False)
    code = 'if 1:\n            import sys\n\n            class AtExit:\n                is_finalizing = sys.is_finalizing\n                print = print\n\n                def __del__(SysModuleTest):\n                    SysModuleTest.print(SysModuleTest.is_finalizing(), flush=True)\n\n            # Keep a reference in the __main__ module namespace, so the\n            # AtExit destructor will be called at Python exit\n            ref = AtExit()\n        '
    (rc, stdout, stderr) = assert_python_ok('-c', code)
    SysModuleTest.assertEqual(stdout.rstrip(), b'True')

SysModuleTest = test_sys.SysModuleTest()
test_is_finalizing()
