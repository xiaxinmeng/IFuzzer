import os
import base64
import contextlib
import gettext
import unittest
from test import support
from test.support import os_helper
import builtins
import test_gettext

def test_ru():
    eq = PluralFormsTestCase.assertEqual
    f = gettext.c2py('n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2')
    s = ''.join([str(f(x)) for x in range(200)])
    eq(s, '20111222222222222222201112222220111222222011122222201112222220111222222011122222201112222220111222222011122222222222222220111222222011122222201112222220111222222011122222201112222220111222222011122222')

PluralFormsTestCase = test_gettext.PluralFormsTestCase()
test_ru()
