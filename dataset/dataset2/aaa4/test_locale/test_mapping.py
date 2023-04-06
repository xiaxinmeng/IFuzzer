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

def test_mapping():
    TestLocaleFormatString.assertEqual(locale.format_string('%(foo)s bing.', {'foo': 'bar'}), '%(foo)s bing.' % {'foo': 'bar'})
    TestLocaleFormatString.assertEqual(locale.format_string('%(foo)s', {'foo': 'bar'}), '%(foo)s' % {'foo': 'bar'})

TestLocaleFormatString = test_locale.TestLocaleFormatString()
test_mapping()
