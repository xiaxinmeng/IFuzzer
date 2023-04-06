import os
import base64
import contextlib
import gettext
import unittest
from test import support
from test.support import os_helper
import builtins
import test_gettext

def test_plural_forms2():
    eq = PluralFormsTestCase.assertEqual
    with open(PluralFormsTestCase.mofile, 'rb') as fp:
        t = gettext.GNUTranslations(fp)
    x = t.ngettext('There is %s file', 'There are %s files', 1)
    eq(x, 'Hay %s fichero')
    x = t.ngettext('There is %s file', 'There are %s files', 2)
    eq(x, 'Hay %s ficheros')

PluralFormsTestCase = test_gettext.PluralFormsTestCase()
PluralFormsTestCase.setUp()
test_plural_forms2()
