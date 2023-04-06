import sys
from textwrap import dedent
from types import FunctionType, MethodType, BuiltinFunctionType
import pyclbr
from unittest import TestCase, main as unittest_main
from test.test_importlib import util as test_importlib_util
import test_pyclbr

def test_dotted_name_not_a_package():
    ReadmoduleTests.assertRaises(ImportError, pyclbr.readmodule_ex, 'asyncio.foo')

ReadmoduleTests = test_pyclbr.ReadmoduleTests()
test_dotted_name_not_a_package()
