import os
import base64
import contextlib
import gettext
import unittest
from test import support
from test.support import os_helper
import builtins
import test_gettext

def test_lv():
    eq = PluralFormsTestCase.assertEqual
    f = gettext.c2py('n%10==1 && n%100!=11 ? 0 : n != 0 ? 1 : 2')
    s = ''.join([str(f(x)) for x in range(200)])
    eq(s, '20111111111111111111101111111110111111111011111111101111111110111111111011111111101111111110111111111011111111111111111110111111111011111111101111111110111111111011111111101111111110111111111011111111')

PluralFormsTestCase = test_gettext.PluralFormsTestCase()
test_lv()
