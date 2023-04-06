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
linux_alpha = (platform.system().startswith('Linux') and
                   platform.machine().startswith('alpha'))
system_round_bug = round(5e15+1) != 5e15+1
@unittest.skipIf(linux_alpha and system_round_bug, 'test will fail;  failure is probably due to a buggy system round function')
def test_round_large():
    BuiltinTest.assertEqual(round(5000000000000000.0 - 1), 5000000000000000.0 - 1)
    BuiltinTest.assertEqual(round(5000000000000000.0), 5000000000000000.0)
    BuiltinTest.assertEqual(round(5000000000000000.0 + 1), 5000000000000000.0 + 1)
    BuiltinTest.assertEqual(round(5000000000000000.0 + 2), 5000000000000000.0 + 2)
    BuiltinTest.assertEqual(round(5000000000000000.0 + 3), 5000000000000000.0 + 3)

BuiltinTest = test_builtin.BuiltinTest()
test_round_large()
