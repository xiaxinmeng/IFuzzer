import os
import base64
import contextlib
import gettext
import unittest
from test import support
from test.support import os_helper
import builtins
import test_gettext

def test_division():
    f = gettext.c2py('2/n*3')
    PluralFormsTestCase.assertEqual(f(1), 6)
    PluralFormsTestCase.assertEqual(f(2), 3)
    PluralFormsTestCase.assertEqual(f(3), 0)
    PluralFormsTestCase.assertEqual(f(-1), -6)
    PluralFormsTestCase.assertRaises(ZeroDivisionError, f, 0)

PluralFormsTestCase = test_gettext.PluralFormsTestCase()
test_division()
