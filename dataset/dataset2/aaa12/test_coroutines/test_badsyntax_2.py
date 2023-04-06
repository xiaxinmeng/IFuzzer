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

def test_badsyntax_2():
    samples = ['def foo():\n                await = 1\n            ', 'class Bar:\n                def async(): pass\n            ', 'class Bar:\n                async = 1\n            ', 'class async:\n                pass\n            ', 'class await:\n                pass\n            ', 'import math as await', 'def async():\n                pass', 'def foo(*, await=1):\n                passasync = 1', 'print(await=1)']
    for code in samples:
        with AsyncBadSyntaxTest.subTest(code=code), AsyncBadSyntaxTest.assertRaises(SyntaxError):
            compile(code, '<test>', 'exec')

AsyncBadSyntaxTest = test_coroutines.AsyncBadSyntaxTest()
test_badsyntax_2()
