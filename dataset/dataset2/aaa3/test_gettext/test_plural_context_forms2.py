import os
import base64
import contextlib
import gettext
import unittest
from test import support
from test.support import os_helper
import builtins
import test_gettext

def test_plural_context_forms2():
    eq = PluralFormsTestCase.assertEqual
    with open(PluralFormsTestCase.mofile, 'rb') as fp:
        t = gettext.GNUTranslations(fp)
    x = t.npgettext('With context', 'There is %s file', 'There are %s files', 1)
    eq(x, 'Hay %s fichero (context)')
    x = t.npgettext('With context', 'There is %s file', 'There are %s files', 2)
    eq(x, 'Hay %s ficheros (context)')

PluralFormsTestCase = test_gettext.PluralFormsTestCase()
PluralFormsTestCase.setUp()
test_plural_context_forms2()
