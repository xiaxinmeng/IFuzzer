import io
import sys
import tempfile
import threading
import unittest
from contextlib import *
from test import support
from test.support import os_helper
import weakref
import test_contextlib

def test_decorating_method():
    context = test_contextlib.mycontext()

    class Test(object):

        @context
        def method(TestContextDecorator, a, b, c=None):
            TestContextDecorator.a = a
            TestContextDecorator.b = b
            TestContextDecorator.c = c
    test = Test()
    test.method(1, 2)
    TestContextDecorator.assertEqual(test.a, 1)
    TestContextDecorator.assertEqual(test.b, 2)
    TestContextDecorator.assertEqual(test.c, None)
    test = Test()
    test.method('a', 'b', 'c')
    TestContextDecorator.assertEqual(test.a, 'a')
    TestContextDecorator.assertEqual(test.b, 'b')
    TestContextDecorator.assertEqual(test.c, 'c')
    test = Test()
    test.method(a=1, b=2)
    TestContextDecorator.assertEqual(test.a, 1)
    TestContextDecorator.assertEqual(test.b, 2)

TestContextDecorator = test_contextlib.TestContextDecorator()
test_decorating_method()
