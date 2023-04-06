import os
import base64
import contextlib
import gettext
import unittest
from test import support
from test.support import os_helper
import builtins
import test_gettext

def test_unicode_context_msgstr():
    t = UnicodeTranslationsTest.pgettext('mycontextÞ', 'abÞ')
    UnicodeTranslationsTest.assertTrue(isinstance(t, str))
    UnicodeTranslationsTest.assertEqual(t, '¤yz (context version)')

UnicodeTranslationsTest = test_gettext.UnicodeTranslationsTest()
UnicodeTranslationsTest.setUp()
test_unicode_context_msgstr()
