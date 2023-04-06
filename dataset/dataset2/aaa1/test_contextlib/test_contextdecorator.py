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

def test_contextdecorator():
    context = test_contextlib.mycontext()
    with context as result:
        TestContextDecorator.assertIs(result, context)
        TestContextDecorator.assertTrue(context.started)
    TestContextDecorator.assertEqual(context.exc, (None, None, None))

TestContextDecorator = test_contextlib.TestContextDecorator()
test_contextdecorator()
