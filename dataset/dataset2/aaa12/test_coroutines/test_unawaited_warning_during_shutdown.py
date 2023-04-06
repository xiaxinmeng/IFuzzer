import contextlib
import copy
import inspect
import pickle
import sys
import types
import unittest
import warnings
from test import support
from test.support import import_helper
from test.support import warnings_helper
from test.support.script_helper import assert_python_ok
from _testcapi import awaitType as at
from _testcapi import awaitType as at
from _testcapi import awaitType as at
import test_coroutines

def test_unawaited_warning_during_shutdown():
    code = 'import asyncio\nasync def f(): pass\nasyncio.gather(f())\n'
    assert_python_ok('-c', code)
    code = 'import sys\nasync def f(): pass\nsys.coro = f()\n'
    assert_python_ok('-c', code)
    code = 'import sys\nasync def f(): pass\nsys.corocycle = [f()]\nsys.corocycle.append(sys.corocycle)\n'
    assert_python_ok('-c', code)

UnawaitedWarningDuringShutdownTest = test_coroutines.UnawaitedWarningDuringShutdownTest()
test_unawaited_warning_during_shutdown()
