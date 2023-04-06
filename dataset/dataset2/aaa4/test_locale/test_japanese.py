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

def test_japanese():
    NormalizeTest.check('ja', 'ja_JP.eucJP')
    NormalizeTest.check('ja.jis', 'ja_JP.JIS7')
    NormalizeTest.check('ja.sjis', 'ja_JP.SJIS')
    NormalizeTest.check('ja_jp', 'ja_JP.eucJP')
    NormalizeTest.check('ja_jp.ajec', 'ja_JP.eucJP')
    NormalizeTest.check('ja_jp.euc', 'ja_JP.eucJP')
    NormalizeTest.check('ja_jp.eucjp', 'ja_JP.eucJP')
    NormalizeTest.check('ja_jp.iso-2022-jp', 'ja_JP.JIS7')
    NormalizeTest.check('ja_jp.iso2022jp', 'ja_JP.JIS7')
    NormalizeTest.check('ja_jp.jis', 'ja_JP.JIS7')
    NormalizeTest.check('ja_jp.jis7', 'ja_JP.JIS7')
    NormalizeTest.check('ja_jp.mscode', 'ja_JP.SJIS')
    NormalizeTest.check('ja_jp.pck', 'ja_JP.SJIS')
    NormalizeTest.check('ja_jp.sjis', 'ja_JP.SJIS')
    NormalizeTest.check('ja_jp.ujis', 'ja_JP.eucJP')
    NormalizeTest.check('ja_jp.utf8', 'ja_JP.UTF-8')
    NormalizeTest.check('japan', 'ja_JP.eucJP')
    NormalizeTest.check('japanese', 'ja_JP.eucJP')
    NormalizeTest.check('japanese-euc', 'ja_JP.eucJP')
    NormalizeTest.check('japanese.euc', 'ja_JP.eucJP')
    NormalizeTest.check('japanese.sjis', 'ja_JP.SJIS')
    NormalizeTest.check('jp_jp', 'ja_JP.eucJP')

NormalizeTest = test_locale.NormalizeTest()
test_japanese()
