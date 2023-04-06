import os
import base64
import contextlib
import gettext
import unittest
from test import support
from test.support import os_helper
import builtins
import test_gettext

def test_de():
    eq = PluralFormsTestCase.assertEqual
    f = gettext.c2py('n != 1')
    s = ''.join([str(f(x)) for x in range(200)])
    eq(s, '10111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111')

PluralFormsTestCase = test_gettext.PluralFormsTestCase()
test_de()
