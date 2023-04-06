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

def test_implementation():
    levels = {'alpha': 10, 'beta': 11, 'candidate': 12, 'final': 15}
    SysModuleTest.assertTrue(hasattr(sys.implementation, 'name'))
    SysModuleTest.assertTrue(hasattr(sys.implementation, 'version'))
    SysModuleTest.assertTrue(hasattr(sys.implementation, 'hexversion'))
    SysModuleTest.assertTrue(hasattr(sys.implementation, 'cache_tag'))
    version = sys.implementation.version
    SysModuleTest.assertEqual(version[:2], (version.major, version.minor))
    hexversion = version.major << 24 | version.minor << 16 | version.micro << 8 | levels[version.releaselevel] << 4 | version.serial << 0
    SysModuleTest.assertEqual(sys.implementation.hexversion, hexversion)
    SysModuleTest.assertEqual(sys.implementation.name, sys.implementation.name.lower())

SysModuleTest = test_sys.SysModuleTest()
test_implementation()
