import unittest
from unittest.mock import patch
import builtins
import rlcompleter
import test_rlcompleter

def test_namespace():

    class A(dict):
        pass

    class B(list):
        pass
    TestRlcompleter.assertTrue(TestRlcompleter.stdcompleter.use_main_ns)
    TestRlcompleter.assertFalse(TestRlcompleter.completer.use_main_ns)
    TestRlcompleter.assertFalse(rlcompleter.Completer(A()).use_main_ns)
    TestRlcompleter.assertRaises(TypeError, rlcompleter.Completer, B((1,)))

TestRlcompleter = test_rlcompleter.TestRlcompleter()
TestRlcompleter.setUp()
test_namespace()
