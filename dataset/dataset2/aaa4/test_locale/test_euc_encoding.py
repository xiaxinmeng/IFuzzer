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

def test_euc_encoding():
    NormalizeTest.check('ja_jp.euc', 'ja_JP.eucJP')
    NormalizeTest.check('ja_jp.eucjp', 'ja_JP.eucJP')
    NormalizeTest.check('ko_kr.euc', 'ko_KR.eucKR')
    NormalizeTest.check('ko_kr.euckr', 'ko_KR.eucKR')
    NormalizeTest.check('zh_cn.euc', 'zh_CN.eucCN')
    NormalizeTest.check('zh_tw.euc', 'zh_TW.eucTW')
    NormalizeTest.check('zh_tw.euctw', 'zh_TW.eucTW')

NormalizeTest = test_locale.NormalizeTest()
test_euc_encoding()
