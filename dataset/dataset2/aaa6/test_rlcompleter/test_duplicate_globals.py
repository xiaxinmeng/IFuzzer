import unittest
from unittest.mock import patch
import builtins
import rlcompleter
import test_rlcompleter

def test_duplicate_globals():
    namespace = {'False': None, 'assert': None, 'try': lambda : None, 'memoryview': None, 'Ellipsis': lambda : None}
    completer = rlcompleter.Completer(namespace)
    TestRlcompleter.assertEqual(completer.complete('False', 0), 'False')
    TestRlcompleter.assertIsNone(completer.complete('False', 1))
    TestRlcompleter.assertEqual(completer.complete('assert', 0), 'assert ')
    TestRlcompleter.assertIsNone(completer.complete('assert', 1))
    TestRlcompleter.assertEqual(completer.complete('try', 0), 'try:')
    TestRlcompleter.assertIsNone(completer.complete('try', 1))
    TestRlcompleter.assertEqual(completer.complete('memoryview', 0), 'memoryview')
    TestRlcompleter.assertIsNone(completer.complete('memoryview', 1))
    TestRlcompleter.assertEqual(completer.complete('Ellipsis', 0), 'Ellipsis()')
    TestRlcompleter.assertIsNone(completer.complete('Ellipsis', 1))

TestRlcompleter = test_rlcompleter.TestRlcompleter()
test_duplicate_globals()
