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

def test_hyphenated_encoding():
    NormalizeTest.check('az_AZ.iso88599e', 'az_AZ.ISO8859-9E')
    NormalizeTest.check('az_AZ.ISO8859-9E', 'az_AZ.ISO8859-9E')
    NormalizeTest.check('tt_RU.koi8c', 'tt_RU.KOI8-C')
    NormalizeTest.check('tt_RU.KOI8-C', 'tt_RU.KOI8-C')
    NormalizeTest.check('lo_LA.cp1133', 'lo_LA.IBM-CP1133')
    NormalizeTest.check('lo_LA.ibmcp1133', 'lo_LA.IBM-CP1133')
    NormalizeTest.check('lo_LA.IBM-CP1133', 'lo_LA.IBM-CP1133')
    NormalizeTest.check('uk_ua.microsoftcp1251', 'uk_UA.CP1251')
    NormalizeTest.check('uk_ua.microsoft-cp1251', 'uk_UA.CP1251')
    NormalizeTest.check('ka_ge.georgianacademy', 'ka_GE.GEORGIAN-ACADEMY')
    NormalizeTest.check('ka_GE.GEORGIAN-ACADEMY', 'ka_GE.GEORGIAN-ACADEMY')
    NormalizeTest.check('cs_CZ.iso88592', 'cs_CZ.ISO8859-2')
    NormalizeTest.check('cs_CZ.ISO8859-2', 'cs_CZ.ISO8859-2')

NormalizeTest = test_locale.NormalizeTest()
test_hyphenated_encoding()
