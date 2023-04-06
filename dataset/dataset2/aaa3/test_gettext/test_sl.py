import os
import base64
import contextlib
import gettext
import unittest
from test import support
from test.support import os_helper
import builtins
import test_gettext

def test_sl():
    eq = PluralFormsTestCase.assertEqual
    f = gettext.c2py('n%100==1 ? 0 : n%100==2 ? 1 : n%100==3 || n%100==4 ? 2 : 3')
    s = ''.join([str(f(x)) for x in range(200)])
    eq(s, '30122333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333012233333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333')

PluralFormsTestCase = test_gettext.PluralFormsTestCase()
test_sl()
