from test.support import check_syntax_error
from test.support.warnings_helper import check_syntax_warning
import inspect
import unittest
import sys
import warnings
from sys import *
import test.ann_module as ann_module
import typing
from collections import ChainMap
from test import ann_module2
import test
from test.support import check_syntax_error
from sys import maxsize
from test.support import check_syntax_error
from test.support.warnings_helper import check_syntax_warning
from test.ann_module3 import f_bad_ann, g_bad_ann, D_bad_ann
import sys
import time, sys
from time import time
from time import time
from sys import path, argv
from sys import path, argv
from sys import path, argv
import sys, time
import test_grammar

def test_async_await():

    async def test():

        def sum():
            pass
        if 1:
            await someobj()
    GrammarTests.assertEqual(test.__name__, 'test')
    GrammarTests.assertTrue(bool(test.__code__.co_flags & inspect.CO_COROUTINE))

    def decorator(func):
        setattr(func, '_marked', True)
        return func

    @decorator
    async def test2():
        return 22
    GrammarTests.assertTrue(test2._marked)
    GrammarTests.assertEqual(test2.__name__, 'test2')
    GrammarTests.assertTrue(bool(test2.__code__.co_flags & inspect.CO_COROUTINE))

GrammarTests = test_grammar.GrammarTests()
test_async_await()
