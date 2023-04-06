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

def test_maybe_new():
    ModuleFinderTest._do_test(test_modulefinder.maybe_test_new)

ModuleFinderTest = test_modulefinder.ModuleFinderTest()
test_maybe_new()
