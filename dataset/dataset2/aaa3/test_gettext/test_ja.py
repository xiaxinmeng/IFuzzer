import os
import base64
import contextlib
import gettext
import unittest
from test import support
from test.support import os_helper
import builtins
import test_gettext

def test_ja():
    eq = PluralFormsTestCase.assertEqual
    f = gettext.c2py('0')
    s = ''.join([str(f(x)) for x in range(200)])
    eq(s, '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

PluralFormsTestCase = test_gettext.PluralFormsTestCase()
test_ja()
