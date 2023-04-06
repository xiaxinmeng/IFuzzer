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

def test_package():
    ModuleFinderTest._do_test(test_modulefinder.package_test)

ModuleFinderTest = test_modulefinder.ModuleFinderTest()
test_package()
