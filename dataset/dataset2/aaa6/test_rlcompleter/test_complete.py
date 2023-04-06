import unittest
from unittest.mock import patch
import builtins
import rlcompleter
import test_rlcompleter

@unittest.mock.patch('rlcompleter._readline_available', False)
def test_complete():
    completer = rlcompleter.Completer()
    TestRlcompleter.assertEqual(completer.complete('', 0), '\t')
    TestRlcompleter.assertEqual(completer.complete('a', 0), 'and ')
    TestRlcompleter.assertEqual(completer.complete('a', 1), 'as ')
    TestRlcompleter.assertEqual(completer.complete('as', 2), 'assert ')
    TestRlcompleter.assertEqual(completer.complete('an', 0), 'and ')
    TestRlcompleter.assertEqual(completer.complete('pa', 0), 'pass')
    TestRlcompleter.assertEqual(completer.complete('Fa', 0), 'False')
    TestRlcompleter.assertEqual(completer.complete('el', 0), 'elif ')
    TestRlcompleter.assertEqual(completer.complete('el', 1), 'else')
    TestRlcompleter.assertEqual(completer.complete('tr', 0), 'try:')

TestRlcompleter = test_rlcompleter.TestRlcompleter()
test_complete()
