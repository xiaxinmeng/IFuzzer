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

def test_cleanup():
    code = 'if 1:\n            import builtins\n            import sys\n\n            class C:\n                def __del__(ShutdownTest):\n                    print("before")\n                    # Check that builtins still exist\n                    len(())\n                    print("after")\n\n            c = C()\n            # Make this module survive until builtins and sys are cleaned\n            builtins.here = sys.modules[__name__]\n            sys.here = sys.modules[__name__]\n            # Create a reference loop so that this module needs to go\n            # through a GC phase.\n            here = sys.modules[__name__]\n            '
    (rc, out, err) = assert_python_ok('-c', code, PYTHONIOENCODING='ascii')
    ShutdownTest.assertEqual(['before', 'after'], out.decode().splitlines())

ShutdownTest = test_builtin.ShutdownTest()
test_cleanup()
