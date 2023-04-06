from test.support import verbose, is_android
from test.support.warnings_helper import check_warnings
import unittest
import locale
import sys
import codecs
import os
import _locale
import os
import test_locale

def test_percent_escape():
    TestLocaleFormatString.assertEqual(locale.format_string('%f%%', 1.0), '%f%%' % 1.0)
    TestLocaleFormatString.assertEqual(locale.format_string('%d %f%%d', (1, 1.0)), '%d %f%%d' % (1, 1.0))
    TestLocaleFormatString.assertEqual(locale.format_string('%(foo)s %%d', {'foo': 'bar'}), '%(foo)s %%d' % {'foo': 'bar'})

TestLocaleFormatString = test_locale.TestLocaleFormatString()
test_percent_escape()
