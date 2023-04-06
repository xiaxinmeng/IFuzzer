import builtins
import collections
import datetime
import functools
import importlib
import inspect
import io
import linecache
import os
from os.path import normcase
import _pickle
import pickle
import shutil
import sys
import types
import textwrap
import unicodedata
import unittest
import unittest.mock
import warnings
from concurrent.futures import ThreadPoolExecutor
from test.support import run_unittest, cpython_only
from test.support import MISSING_C_DOCSTRINGS, ALWAYS_EQ
from test.support.import_helper import DirsOnSysPath
from test.support.os_helper import TESTFN
from test.support.script_helper import assert_python_ok, assert_python_failure
from test import inspect_fodder as mod
from test import inspect_fodder2 as mod2
from test import support
from test.test_import import _ready_to_import
from abc import ABCMeta, abstractmethod
from abc import ABCMeta, abstractmethod
from types import ModuleType
import asyncio

import _testcapi
import _testcapi
import _testcapi
import _testcapi
import _testcapi
from functools import partial
from functools import partialmethod
import functools
import test_inspect

def test_varkw_only():
    f = TestGetcallargsFunctions.makeCallable('**c')
    TestGetcallargsFunctions.assertEqualCallArgs(f, '')
    TestGetcallargsFunctions.assertEqualCallArgs(f, 'a=1')
    TestGetcallargsFunctions.assertEqualCallArgs(f, 'a=1, b=2')
    TestGetcallargsFunctions.assertEqualCallArgs(f, 'c=3, **{"a": 1, "b": 2}')
    TestGetcallargsFunctions.assertEqualCallArgs(f, '**collections.UserDict(a=1, b=2)')
    TestGetcallargsFunctions.assertEqualCallArgs(f, 'c=3, **collections.UserDict(a=1, b=2)')

TestGetcallargsFunctions = test_inspect.TestGetcallargsFunctions()
test_varkw_only()
