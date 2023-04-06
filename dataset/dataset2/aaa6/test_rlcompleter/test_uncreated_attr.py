import unittest
from unittest.mock import patch
import builtins
import rlcompleter
import test_rlcompleter

def test_uncreated_attr():

    class Foo:
        __slots__ = ('bar',)
    completer = rlcompleter.Completer(dict(f=Foo()))
    TestRlcompleter.assertEqual(completer.complete('f.', 0), 'f.bar')

TestRlcompleter = test_rlcompleter.TestRlcompleter()
test_uncreated_attr()
