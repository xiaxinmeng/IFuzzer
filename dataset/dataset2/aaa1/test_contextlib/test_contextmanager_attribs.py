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

def test_contextmanager_attribs():
    baz = ContextManagerTestCase._create_contextmanager_attribs()
    ContextManagerTestCase.assertEqual(baz.__name__, 'baz')
    ContextManagerTestCase.assertEqual(baz.foo, 'bar')

ContextManagerTestCase = test_contextlib.ContextManagerTestCase()
test_contextmanager_attribs()
