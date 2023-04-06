import sys
from textwrap import dedent
from types import FunctionType, MethodType, BuiltinFunctionType
import pyclbr
from unittest import TestCase, main as unittest_main
from test.test_importlib import util as test_importlib_util
import test_pyclbr

def test_easy():
    PyclbrTest.checkModule('pyclbr')
    PyclbrTest.checkModule('doctest', ignore=('TestResults', '_SpoofOut', 'DocTestCase', '_DocTestSuite'))
    PyclbrTest.checkModule('difflib', ignore=('Match',))

PyclbrTest = test_pyclbr.PyclbrTest()
test_easy()
