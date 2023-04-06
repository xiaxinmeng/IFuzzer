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

@unittest.skipIf(sys.flags.ignore_environment, '-E was given')
def test_envar_good_path_builtin():
    TestBreakpoint.env['PYTHONBREAKPOINT'] = 'int'
    with patch('builtins.int') as mock:
        breakpoint('7')
        mock.assert_called_once_with('7')

TestBreakpoint = test_builtin.TestBreakpoint()
TestBreakpoint.setUp()
test_envar_good_path_builtin()
