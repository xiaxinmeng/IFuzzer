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

def test_decorator():
    context = test_contextlib.mycontext()

    @context
    def test():
        TestContextDecorator.assertIsNone(context.exc)
        TestContextDecorator.assertTrue(context.started)
    test()
    TestContextDecorator.assertEqual(context.exc, (None, None, None))

TestContextDecorator = test_contextlib.TestContextDecorator()
test_decorator()
