import unittest
from unittest.mock import patch
import builtins
import rlcompleter
import test_rlcompleter

def test_global_matches():
    TestRlcompleter.assertEqual(sorted(TestRlcompleter.stdcompleter.global_matches('di')), [x + '(' for x in dir(builtins) if x.startswith('di')])
    TestRlcompleter.assertEqual(sorted(TestRlcompleter.stdcompleter.global_matches('st')), [x + '(' for x in dir(builtins) if x.startswith('st')])
    TestRlcompleter.assertEqual(TestRlcompleter.stdcompleter.global_matches('akaksajadhak'), [])
    TestRlcompleter.assertEqual(TestRlcompleter.completer.global_matches('CompleteM'), ['CompleteMe()'])
    TestRlcompleter.assertEqual(TestRlcompleter.completer.global_matches('eg'), ['egg('])
    TestRlcompleter.assertEqual(TestRlcompleter.completer.global_matches('CompleteM'), ['CompleteMe()'])

TestRlcompleter = test_rlcompleter.TestRlcompleter()
TestRlcompleter.setUp()
test_global_matches()
