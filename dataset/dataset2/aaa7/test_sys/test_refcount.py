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

@test.support.refcount_test
def test_refcount():
    global n
    SysModuleTest.assertRaises(TypeError, sys.getrefcount)
    c = sys.getrefcount(None)
    n = None
    SysModuleTest.assertEqual(sys.getrefcount(None), c + 1)
    del n
    SysModuleTest.assertEqual(sys.getrefcount(None), c)
    if hasattr(sys, 'gettotalrefcount'):
        SysModuleTest.assertIsInstance(sys.gettotalrefcount(), int)

SysModuleTest = test_sys.SysModuleTest()
test_refcount()
