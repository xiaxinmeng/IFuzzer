import os
import base64
import contextlib
import gettext
import unittest
from test import support
from test.support import os_helper
import builtins
import test_gettext

def test_plural_context_forms1():
    eq = PluralFormsTestCase.assertEqual
    x = gettext.npgettext('With context', 'There is %s file', 'There are %s files', 1)
    eq(x, 'Hay %s fichero (context)')
    x = gettext.npgettext('With context', 'There is %s file', 'There are %s files', 2)
    eq(x, 'Hay %s ficheros (context)')

PluralFormsTestCase = test_gettext.PluralFormsTestCase()
test_plural_context_forms1()
