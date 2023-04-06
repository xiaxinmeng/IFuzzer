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

@unittest.skipUnless(hasattr(sys, 'getandroidapilevel'), 'need sys.getandroidapilevel()')
def test_getandroidapilevel():
    level = sys.getandroidapilevel()
    SysModuleTest.assertIsInstance(level, int)
    SysModuleTest.assertGreater(level, 0)

SysModuleTest = test_sys.SysModuleTest()
test_getandroidapilevel()
