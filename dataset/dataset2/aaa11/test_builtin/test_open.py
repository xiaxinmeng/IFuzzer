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

def test_open():
    BuiltinTest.write_testfile()
    fp = open(TESTFN, 'r')
    with fp:
        BuiltinTest.assertEqual(fp.readline(4), '1+1\n')
        BuiltinTest.assertEqual(fp.readline(), 'The quick brown fox jumps over the lazy dog.\n')
        BuiltinTest.assertEqual(fp.readline(4), 'Dear')
        BuiltinTest.assertEqual(fp.readline(100), ' John\n')
        BuiltinTest.assertEqual(fp.read(300), 'XXX' * 100)
        BuiltinTest.assertEqual(fp.read(1000), 'YYY' * 100)
    BuiltinTest.assertRaises(ValueError, open, 'a\x00b')
    BuiltinTest.assertRaises(ValueError, open, b'a\x00b')

BuiltinTest = test_builtin.BuiltinTest()
test_open()
