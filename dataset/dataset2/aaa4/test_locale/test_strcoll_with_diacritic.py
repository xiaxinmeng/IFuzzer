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

@unittest.skipIf(sys.platform.startswith('aix'), 'bpo-29972: broken test on AIX')
def test_strcoll_with_diacritic():
    TestEnUSCollation.assertLess(locale.strcoll('à', 'b'), 0)

TestEnUSCollation = test_locale.TestEnUSCollation()
test_strcoll_with_diacritic()
