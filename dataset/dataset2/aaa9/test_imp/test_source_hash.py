import importlib
import importlib.util
import os
import os.path
import py_compile
import sys
from test import support
from test.support import import_helper
from test.support import os_helper
from test.support import script_helper
import unittest
import warnings
import imp
import _imp
import _frozen_importlib_external
import _frozen_importlib
import os
import time
import marshal
from html import parser
import test_imp

def test_source_hash():
    ImportTests.assertEqual(_imp.source_hash(42, b'hi'), b'\xc6\xe7Z\r\x03:}\xab')
    ImportTests.assertEqual(_imp.source_hash(43, b'hi'), b'\x85\x9765\xf8\x9a\x8b9')

ImportTests = test_imp.ImportTests()
test_source_hash()
