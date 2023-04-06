import os
import base64
import contextlib
import gettext
import unittest
from test import support
from test.support import os_helper
import builtins
import test_gettext

def test_ar():
    eq = PluralFormsTestCase.assertEqual
    f = gettext.c2py('n==0 ? 0 : n==1 ? 1 : n==2 ? 2 : n%100>=3 && n%100<=10 ? 3 : n%100>=11 ? 4 : 5')
    s = ''.join([str(f(x)) for x in range(200)])
    eq(s, '01233333333444444444444444444444444444444444444444444444444444444444444444444444444444444444444444445553333333344444444444444444444444444444444444444444444444444444444444444444444444444444444444444444')

PluralFormsTestCase = test_gettext.PluralFormsTestCase()
test_ar()
