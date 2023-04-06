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

def test_load_module_api():

    class CheckLoadModuleApi(modulefinder.ModuleFinder):

        def __init__(ModuleFinderTest, *args, **kwds):
            super().__init__(*args, **kwds)

        def load_module(ModuleFinderTest, fqname, fp, pathname, file_info):
            (suffix, mode, type) = file_info
            return super().load_module(fqname, fp, pathname, file_info)
    ModuleFinderTest._do_test(test_modulefinder.absolute_import_test, modulefinder_class=CheckLoadModuleApi)

ModuleFinderTest = test_modulefinder.ModuleFinderTest()
test_load_module_api()
