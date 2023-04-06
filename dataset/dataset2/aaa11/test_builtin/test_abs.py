import ast
import asyncio
import builtins
import collections
import decimal
import fractions
import gc
import io
import locale
import os
import pickle
import platform
import random
import re
import sys
import traceback
import types
import unittest
import warnings
from contextlib import ExitStack
from functools import partial
from inspect import CO_COROUTINE
from itertools import product
from textwrap import dedent
from types import AsyncGeneratorType, FunctionType
from operator import neg
from test import support
from test.support import swap_attr, maybe_get_event_loop_policy
from test.support.os_helper import EnvironmentVarGuard, TESTFN, unlink
from test.support.script_helper import assert_python_ok
from test.support.warnings_helper import check_warnings
from unittest.mock import MagicMock, patch
import pty, signal
from math import sqrt
from doctest import DocTestSuite
import test_builtin

def test_abs():
    BuiltinTest.assertEqual(abs(0), 0)
    BuiltinTest.assertEqual(abs(1234), 1234)
    BuiltinTest.assertEqual(abs(-1234), 1234)
    BuiltinTest.assertTrue(abs(-sys.maxsize - 1) > 0)
    BuiltinTest.assertEqual(abs(0.0), 0.0)
    BuiltinTest.assertEqual(abs(3.14), 3.14)
    BuiltinTest.assertEqual(abs(-3.14), 3.14)
    BuiltinTest.assertRaises(TypeError, abs, 'a')
    BuiltinTest.assertEqual(abs(True), 1)
    BuiltinTest.assertEqual(abs(False), 0)
    BuiltinTest.assertRaises(TypeError, abs)
    BuiltinTest.assertRaises(TypeError, abs, None)

    class AbsClass(object):

        def __abs__(BuiltinTest):
            return -5
    BuiltinTest.assertEqual(abs(AbsClass()), -5)

BuiltinTest = test_builtin.BuiltinTest()
test_abs()
