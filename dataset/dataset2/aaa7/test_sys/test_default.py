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

def test_default():
    size = test.support.calcvobjsize
    SizeofTest.assertEqual(sys.getsizeof(True), size('') + SizeofTest.longdigit)
    SizeofTest.assertEqual(sys.getsizeof(True, -1), size('') + SizeofTest.longdigit)

SizeofTest = test_sys.SizeofTest()
SizeofTest.setUp()
test_default()
