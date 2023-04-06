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

def test_decorator_with_exception():
    context = test_contextlib.mycontext()

    @context
    def test():
        TestContextDecorator.assertIsNone(context.exc)
        TestContextDecorator.assertTrue(context.started)
        raise NameError('foo')
    with TestContextDecorator.assertRaisesRegex(NameError, 'foo'):
        test()
    TestContextDecorator.assertIsNotNone(context.exc)
    TestContextDecorator.assertIs(context.exc[0], NameError)

TestContextDecorator = test_contextlib.TestContextDecorator()
test_decorator_with_exception()
