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

@support.requires_docstrings
def test_contextmanager_doc_attrib():
    baz = ContextManagerTestCase._create_contextmanager_attribs()
    ContextManagerTestCase.assertEqual(baz.__doc__, 'Whee!')

ContextManagerTestCase = test_contextlib.ContextManagerTestCase()
test_contextmanager_doc_attrib()
