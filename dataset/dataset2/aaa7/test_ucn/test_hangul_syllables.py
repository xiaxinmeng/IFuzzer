import ast
import unittest
import unicodedata
from test import support
from http.client import HTTPException
from _testcapi import INT_MAX, PY_SSIZE_T_MAX, UINT_MAX
import test_ucn

def test_hangul_syllables():
    UnicodeNamesTest.checkletter('HANGUL SYLLABLE GA', '가')
    UnicodeNamesTest.checkletter('HANGUL SYLLABLE GGWEOSS', '꿨')
    UnicodeNamesTest.checkletter('HANGUL SYLLABLE DOLS', '돐')
    UnicodeNamesTest.checkletter('HANGUL SYLLABLE RYAN', '랸')
    UnicodeNamesTest.checkletter('HANGUL SYLLABLE MWIK', '뮠')
    UnicodeNamesTest.checkletter('HANGUL SYLLABLE BBWAEM', '뾈')
    UnicodeNamesTest.checkletter('HANGUL SYLLABLE SSEOL', '썰')
    UnicodeNamesTest.checkletter('HANGUL SYLLABLE YI', '의')
    UnicodeNamesTest.checkletter('HANGUL SYLLABLE JJYOSS', '쭀')
    UnicodeNamesTest.checkletter('HANGUL SYLLABLE KYEOLS', '켨')
    UnicodeNamesTest.checkletter('HANGUL SYLLABLE PAN', '판')
    UnicodeNamesTest.checkletter('HANGUL SYLLABLE HWEOK', '훸')
    UnicodeNamesTest.checkletter('HANGUL SYLLABLE HIH', '힣')
    UnicodeNamesTest.assertRaises(ValueError, unicodedata.name, '\ud7a4')

UnicodeNamesTest = test_ucn.UnicodeNamesTest()
test_hangul_syllables()
