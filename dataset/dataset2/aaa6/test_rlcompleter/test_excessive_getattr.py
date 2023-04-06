import unittest
from unittest.mock import patch
import builtins
import rlcompleter
import test_rlcompleter

def test_excessive_getattr():

    class Foo:
        calls = 0

        @property
        def bar(TestRlcompleter):
            TestRlcompleter.calls += 1
            return None
    f = Foo()
    completer = rlcompleter.Completer(dict(f=f))
    TestRlcompleter.assertEqual(completer.complete('f.b', 0), 'f.bar')
    TestRlcompleter.assertEqual(f.calls, 1)

TestRlcompleter = test_rlcompleter.TestRlcompleter()
test_excessive_getattr()
