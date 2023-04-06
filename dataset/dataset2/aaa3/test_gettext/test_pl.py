import os
import base64
import contextlib
import gettext
import unittest
from test import support
from test.support import os_helper
import builtins
import test_gettext

def test_pl():
    eq = PluralFormsTestCase.assertEqual
    f = gettext.c2py('n==1 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2')
    s = ''.join([str(f(x)) for x in range(200)])
    eq(s, '20111222222222222222221112222222111222222211122222221112222222111222222211122222221112222222111222222211122222222222222222111222222211122222221112222222111222222211122222221112222222111222222211122222')

PluralFormsTestCase = test_gettext.PluralFormsTestCase()
test_pl()
