import unittest
from test import badsyntax_3131
import test_unicode_identifiers

def test_invalid():
    try:
        from test import badsyntax_3131
    except SyntaxError as err:
        PEP3131Test.assertEqual(str(err), "invalid character '€' (U+20AC) (badsyntax_3131.py, line 2)")
        PEP3131Test.assertEqual(err.lineno, 2)
        PEP3131Test.assertEqual(err.offset, 1)
    else:
        PEP3131Test.fail("expected exception didn't occur")

PEP3131Test = test_unicode_identifiers.PEP3131Test()
test_invalid()
