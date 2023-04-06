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

def test_tp_await_2():
    from _testcapi import awaitType as at
    future = at(iter([1]))
    CAPITest.assertEqual(next(future.__await__()), 1)

CAPITest = test_coroutines.CAPITest()
test_tp_await_2()
