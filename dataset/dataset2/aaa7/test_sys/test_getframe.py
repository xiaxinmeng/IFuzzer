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

def test_getframe():
    SysModuleTest.assertRaises(TypeError, sys._getframe, 42, 42)
    SysModuleTest.assertRaises(ValueError, sys._getframe, 2000000000)
    SysModuleTest.assertTrue(SysModuleTest.test_getframe.__code__ is sys._getframe().f_code)

SysModuleTest = test_sys.SysModuleTest()
test_getframe()
