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

def test_relative_imports_4():
    ModuleFinderTest._do_test(test_modulefinder.relative_import_test_4)

ModuleFinderTest = test_modulefinder.ModuleFinderTest()
test_relative_imports_4()
