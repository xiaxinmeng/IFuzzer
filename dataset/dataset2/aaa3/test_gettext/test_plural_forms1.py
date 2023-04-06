import os
import base64
import contextlib
import gettext
import unittest
from test import support
from test.support import os_helper
import builtins
import test_gettext

def test_plural_forms1():
    eq = PluralFormsTestCase.assertEqual
    x = gettext.ngettext('There is %s file', 'There are %s files', 1)
    eq(x, 'Hay %s fichero')
    x = gettext.ngettext('There is %s file', 'There are %s files', 2)
    eq(x, 'Hay %s ficheros')

PluralFormsTestCase = test_gettext.PluralFormsTestCase()
test_plural_forms1()
