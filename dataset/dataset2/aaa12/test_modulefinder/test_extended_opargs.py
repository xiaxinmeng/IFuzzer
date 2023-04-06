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

def test_extended_opargs():
    extended_opargs_test = ['a', ['a', 'b'], [], [], 'a.py\n                                %r\n                                import b\nb.py\n' % list(range(2 ** 16))]
    ModuleFinderTest._do_test(extended_opargs_test)

ModuleFinderTest = test_modulefinder.ModuleFinderTest()
test_extended_opargs()
