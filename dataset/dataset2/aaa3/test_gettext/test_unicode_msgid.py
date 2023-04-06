import os
import base64
import contextlib
import gettext
import unittest
from test import support
from test.support import os_helper
import builtins
import test_gettext

def test_unicode_msgid():
    unless = UnicodeTranslationsTest.assertTrue
    unless(isinstance(UnicodeTranslationsTest.ngettext('', '', 1), str))
    unless(isinstance(UnicodeTranslationsTest.ngettext('', '', 2), str))

UnicodeTranslationsTest = test_gettext.UnicodeTranslationsTest()
UnicodeTranslationsTest.setUp()
test_unicode_msgid()
