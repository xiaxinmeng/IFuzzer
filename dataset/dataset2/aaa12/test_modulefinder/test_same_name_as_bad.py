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

def test_same_name_as_bad():
    ModuleFinderTest._do_test(test_modulefinder.same_name_as_bad_test)

ModuleFinderTest = test_modulefinder.ModuleFinderTest()
test_same_name_as_bad()
