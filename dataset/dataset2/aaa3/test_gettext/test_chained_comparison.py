import os
import base64
import contextlib
import gettext
import unittest
from test import support
from test.support import os_helper
import builtins
import test_gettext

def test_chained_comparison():
    f = gettext.c2py('n == n == n')
    PluralFormsTestCase.assertEqual(''.join((str(f(x)) for x in range(3))), '010')
    f = gettext.c2py('1 < n == n')
    PluralFormsTestCase.assertEqual(''.join((str(f(x)) for x in range(3))), '100')
    f = gettext.c2py('n == n < 2')
    PluralFormsTestCase.assertEqual(''.join((str(f(x)) for x in range(3))), '010')
    f = gettext.c2py('0 < n < 2')
    PluralFormsTestCase.assertEqual(''.join((str(f(x)) for x in range(3))), '111')

PluralFormsTestCase = test_gettext.PluralFormsTestCase()
test_chained_comparison()
