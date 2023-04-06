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

def test_contextdecorator_with_exception():
    context = test_contextlib.mycontext()
    with TestContextDecorator.assertRaisesRegex(NameError, 'foo'):
        with context:
            raise NameError('foo')
    TestContextDecorator.assertIsNotNone(context.exc)
    TestContextDecorator.assertIs(context.exc[0], NameError)
    context = test_contextlib.mycontext()
    context.catch = True
    with context:
        raise NameError('foo')
    TestContextDecorator.assertIsNotNone(context.exc)
    TestContextDecorator.assertIs(context.exc[0], NameError)

TestContextDecorator = test_contextlib.TestContextDecorator()
test_contextdecorator_with_exception()
