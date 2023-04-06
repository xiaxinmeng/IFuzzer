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

def test_tp_await_1():
    from _testcapi import awaitType as at

    async def foo():
        future = at(iter([1]))
        return await future
    CAPITest.assertEqual(foo().send(None), 1)

CAPITest = test_coroutines.CAPITest()
test_tp_await_1()
