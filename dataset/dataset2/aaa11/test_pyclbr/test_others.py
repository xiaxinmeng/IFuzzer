import sys
from textwrap import dedent
from types import FunctionType, MethodType, BuiltinFunctionType
import pyclbr
from unittest import TestCase, main as unittest_main
from test.test_importlib import util as test_importlib_util
import test_pyclbr

def test_others():
    cm = PyclbrTest.checkModule
    cm('random', ignore=('Random',))
    cm('cgi', ignore=('log',))
    cm('pickle', ignore=('partial', 'PickleBuffer'))
    cm('aifc', ignore=('_aifc_params',))
    cm('sre_parse', ignore=('dump', 'groups', 'pos'))
    cm('pdb')
    cm('pydoc', ignore=('input', 'output'))
    cm('email.parser')
    cm('test.test_pyclbr')

PyclbrTest = test_pyclbr.PyclbrTest()
test_others()
