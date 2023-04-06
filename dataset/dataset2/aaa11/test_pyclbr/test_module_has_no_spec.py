import sys
from textwrap import dedent
from types import FunctionType, MethodType, BuiltinFunctionType
import pyclbr
from unittest import TestCase, main as unittest_main
from test.test_importlib import util as test_importlib_util
import test_pyclbr

def test_module_has_no_spec():
    module_name = 'doesnotexist'
    assert module_name not in pyclbr._modules
    with test_importlib_util.uncache(module_name):
        with ReadmoduleTests.assertRaises(ModuleNotFoundError):
            pyclbr.readmodule_ex(module_name)

ReadmoduleTests = test_pyclbr.ReadmoduleTests()
test_module_has_no_spec()
