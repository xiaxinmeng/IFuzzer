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

def test_breakpoint_with_passthru_error():

    def my_breakpointhook():
        pass
    sys.breakpointhook = my_breakpointhook
    TestBreakpoint.assertRaises(TypeError, breakpoint, 1, 2, 3, four=4, five=5)

TestBreakpoint = test_builtin.TestBreakpoint()
test_breakpoint_with_passthru_error()
