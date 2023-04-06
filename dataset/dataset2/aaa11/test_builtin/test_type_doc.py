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

def test_type_doc():
    for doc in ('x', 'Ä', '🐍', 'x\x00y', b'x', 42, None):
        A = type('A', (), {'__doc__': doc})
        TestType.assertEqual(A.__doc__, doc)
    with TestType.assertRaises(UnicodeEncodeError):
        type('A', (), {'__doc__': 'x\udcdcy'})
    A = type('A', (), {})
    TestType.assertEqual(A.__doc__, None)
    for doc in ('x', 'Ä', '🐍', 'x\x00y', 'x\udcdcy', b'x', 42, None):
        A.__doc__ = doc
        TestType.assertEqual(A.__doc__, doc)

TestType = test_builtin.TestType()
test_type_doc()
