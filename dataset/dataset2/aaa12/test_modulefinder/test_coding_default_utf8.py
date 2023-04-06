import os
import errno
import importlib.machinery
import py_compile
import shutil
import unittest
import tempfile
from test import support
import modulefinder
import test_modulefinder

def test_coding_default_utf8():
    ModuleFinderTest._do_test(test_modulefinder.coding_default_utf8_test)

ModuleFinderTest = test_modulefinder.ModuleFinderTest()
test_coding_default_utf8()
