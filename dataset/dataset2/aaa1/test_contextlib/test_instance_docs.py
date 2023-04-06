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
def test_instance_docs():
    cm_docstring = suppress.__doc__
    obj = suppress()
    ClosingTestCase.assertEqual(obj.__doc__, cm_docstring)

ClosingTestCase = test_contextlib.ClosingTestCase()
test_instance_docs()
