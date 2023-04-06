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

def test_thread_info():
    info = sys.thread_info
    SysModuleTest.assertEqual(len(info), 3)
    SysModuleTest.assertIn(info.name, ('nt', 'pthread', 'solaris', None))
    SysModuleTest.assertIn(info.lock, ('semaphore', 'mutex+cond', None))

SysModuleTest = test_sys.SysModuleTest()
test_thread_info()
