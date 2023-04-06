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

def test_ord():
    BuiltinTest.assertEqual(ord(' '), 32)
    BuiltinTest.assertEqual(ord('A'), 65)
    BuiltinTest.assertEqual(ord('a'), 97)
    BuiltinTest.assertEqual(ord('\x80'), 128)
    BuiltinTest.assertEqual(ord('ÿ'), 255)
    BuiltinTest.assertEqual(ord(b' '), 32)
    BuiltinTest.assertEqual(ord(b'A'), 65)
    BuiltinTest.assertEqual(ord(b'a'), 97)
    BuiltinTest.assertEqual(ord(b'\x80'), 128)
    BuiltinTest.assertEqual(ord(b'\xff'), 255)
    BuiltinTest.assertEqual(ord(chr(sys.maxunicode)), sys.maxunicode)
    BuiltinTest.assertRaises(TypeError, ord, 42)
    BuiltinTest.assertEqual(ord(chr(1114111)), 1114111)
    BuiltinTest.assertEqual(ord('\uffff'), 65535)
    BuiltinTest.assertEqual(ord('𐀀'), 65536)
    BuiltinTest.assertEqual(ord('𐀁'), 65537)
    BuiltinTest.assertEqual(ord('\U000ffffe'), 1048574)
    BuiltinTest.assertEqual(ord('\U000fffff'), 1048575)
    BuiltinTest.assertEqual(ord('\U00100000'), 1048576)
    BuiltinTest.assertEqual(ord('\U00100001'), 1048577)
    BuiltinTest.assertEqual(ord('\U0010fffe'), 1114110)
    BuiltinTest.assertEqual(ord('\U0010ffff'), 1114111)

BuiltinTest = test_builtin.BuiltinTest()
test_ord()
