import os
import base64
import contextlib
import gettext
import unittest
from test import support
from test.support import os_helper
import builtins
import test_gettext

def test_unicode_context_msgid():
    unless = UnicodeTranslationsPluralTest.assertTrue
    unless(isinstance(UnicodeTranslationsPluralTest.npgettext('', '', '', 1), str))
    unless(isinstance(UnicodeTranslationsPluralTest.npgettext('', '', '', 2), str))

UnicodeTranslationsPluralTest = test_gettext.UnicodeTranslationsPluralTest()
UnicodeTranslationsPluralTest.setUp()
test_unicode_context_msgid()
