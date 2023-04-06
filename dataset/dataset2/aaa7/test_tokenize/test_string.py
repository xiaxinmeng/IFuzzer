from test import support
from test.support import os_helper
from tokenize import tokenize, _tokenize, untokenize, NUMBER, NAME, OP, STRING, ENDMARKER, ENCODING, tok_name, detect_encoding, open as tokenize_open, Untokenizer, generate_tokens, NEWLINE
from io import BytesIO, StringIO
import unittest
from unittest import TestCase, mock
from test.test_grammar import VALID_UNDERSCORE_LITERALS, INVALID_UNDERSCORE_LITERALS
import os
import token
from decimal import Decimal
import tokenize as tokenize_module
import glob, random
import test_tokenize

def test_string():
    TokenizeTest.check_tokenize('x = \'\'; y = ""', '    NAME       \'x\'           (1, 0) (1, 1)\n    OP         \'=\'           (1, 2) (1, 3)\n    STRING     "\'\'"          (1, 4) (1, 6)\n    OP         \';\'           (1, 6) (1, 7)\n    NAME       \'y\'           (1, 8) (1, 9)\n    OP         \'=\'           (1, 10) (1, 11)\n    STRING     \'""\'          (1, 12) (1, 14)\n    ')
    TokenizeTest.check_tokenize('x = \'"\'; y = "\'"', '    NAME       \'x\'           (1, 0) (1, 1)\n    OP         \'=\'           (1, 2) (1, 3)\n    STRING     \'\\\'"\\\'\'       (1, 4) (1, 7)\n    OP         \';\'           (1, 7) (1, 8)\n    NAME       \'y\'           (1, 9) (1, 10)\n    OP         \'=\'           (1, 11) (1, 12)\n    STRING     \'"\\\'"\'        (1, 13) (1, 16)\n    ')
    TokenizeTest.check_tokenize('x = "doesn\'t "shrink", does it"', '    NAME       \'x\'           (1, 0) (1, 1)\n    OP         \'=\'           (1, 2) (1, 3)\n    STRING     \'"doesn\\\'t "\' (1, 4) (1, 14)\n    NAME       \'shrink\'      (1, 14) (1, 20)\n    STRING     \'", does it"\' (1, 20) (1, 31)\n    ')
    TokenizeTest.check_tokenize("x = 'abc' + 'ABC'", '    NAME       \'x\'           (1, 0) (1, 1)\n    OP         \'=\'           (1, 2) (1, 3)\n    STRING     "\'abc\'"       (1, 4) (1, 9)\n    OP         \'+\'           (1, 10) (1, 11)\n    STRING     "\'ABC\'"       (1, 12) (1, 17)\n    ')
    TokenizeTest.check_tokenize('y = "ABC" + "ABC"', '    NAME       \'y\'           (1, 0) (1, 1)\n    OP         \'=\'           (1, 2) (1, 3)\n    STRING     \'"ABC"\'       (1, 4) (1, 9)\n    OP         \'+\'           (1, 10) (1, 11)\n    STRING     \'"ABC"\'       (1, 12) (1, 17)\n    ')
    TokenizeTest.check_tokenize("x = r'abc' + r'ABC' + R'ABC' + R'ABC'", '    NAME       \'x\'           (1, 0) (1, 1)\n    OP         \'=\'           (1, 2) (1, 3)\n    STRING     "r\'abc\'"      (1, 4) (1, 10)\n    OP         \'+\'           (1, 11) (1, 12)\n    STRING     "r\'ABC\'"      (1, 13) (1, 19)\n    OP         \'+\'           (1, 20) (1, 21)\n    STRING     "R\'ABC\'"      (1, 22) (1, 28)\n    OP         \'+\'           (1, 29) (1, 30)\n    STRING     "R\'ABC\'"      (1, 31) (1, 37)\n    ')
    TokenizeTest.check_tokenize('y = r"abc" + r"ABC" + R"ABC" + R"ABC"', '    NAME       \'y\'           (1, 0) (1, 1)\n    OP         \'=\'           (1, 2) (1, 3)\n    STRING     \'r"abc"\'      (1, 4) (1, 10)\n    OP         \'+\'           (1, 11) (1, 12)\n    STRING     \'r"ABC"\'      (1, 13) (1, 19)\n    OP         \'+\'           (1, 20) (1, 21)\n    STRING     \'R"ABC"\'      (1, 22) (1, 28)\n    OP         \'+\'           (1, 29) (1, 30)\n    STRING     \'R"ABC"\'      (1, 31) (1, 37)\n    ')
    TokenizeTest.check_tokenize("u'abc' + U'abc'", '    STRING     "u\'abc\'"      (1, 0) (1, 6)\n    OP         \'+\'           (1, 7) (1, 8)\n    STRING     "U\'abc\'"      (1, 9) (1, 15)\n    ')
    TokenizeTest.check_tokenize('u"abc" + U"abc"', '    STRING     \'u"abc"\'      (1, 0) (1, 6)\n    OP         \'+\'           (1, 7) (1, 8)\n    STRING     \'U"abc"\'      (1, 9) (1, 15)\n    ')
    TokenizeTest.check_tokenize("b'abc' + B'abc'", '    STRING     "b\'abc\'"      (1, 0) (1, 6)\n    OP         \'+\'           (1, 7) (1, 8)\n    STRING     "B\'abc\'"      (1, 9) (1, 15)\n    ')
    TokenizeTest.check_tokenize('b"abc" + B"abc"', '    STRING     \'b"abc"\'      (1, 0) (1, 6)\n    OP         \'+\'           (1, 7) (1, 8)\n    STRING     \'B"abc"\'      (1, 9) (1, 15)\n    ')
    TokenizeTest.check_tokenize("br'abc' + bR'abc' + Br'abc' + BR'abc'", '    STRING     "br\'abc\'"     (1, 0) (1, 7)\n    OP         \'+\'           (1, 8) (1, 9)\n    STRING     "bR\'abc\'"     (1, 10) (1, 17)\n    OP         \'+\'           (1, 18) (1, 19)\n    STRING     "Br\'abc\'"     (1, 20) (1, 27)\n    OP         \'+\'           (1, 28) (1, 29)\n    STRING     "BR\'abc\'"     (1, 30) (1, 37)\n    ')
    TokenizeTest.check_tokenize('br"abc" + bR"abc" + Br"abc" + BR"abc"', '    STRING     \'br"abc"\'     (1, 0) (1, 7)\n    OP         \'+\'           (1, 8) (1, 9)\n    STRING     \'bR"abc"\'     (1, 10) (1, 17)\n    OP         \'+\'           (1, 18) (1, 19)\n    STRING     \'Br"abc"\'     (1, 20) (1, 27)\n    OP         \'+\'           (1, 28) (1, 29)\n    STRING     \'BR"abc"\'     (1, 30) (1, 37)\n    ')
    TokenizeTest.check_tokenize("rb'abc' + rB'abc' + Rb'abc' + RB'abc'", '    STRING     "rb\'abc\'"     (1, 0) (1, 7)\n    OP         \'+\'           (1, 8) (1, 9)\n    STRING     "rB\'abc\'"     (1, 10) (1, 17)\n    OP         \'+\'           (1, 18) (1, 19)\n    STRING     "Rb\'abc\'"     (1, 20) (1, 27)\n    OP         \'+\'           (1, 28) (1, 29)\n    STRING     "RB\'abc\'"     (1, 30) (1, 37)\n    ')
    TokenizeTest.check_tokenize('rb"abc" + rB"abc" + Rb"abc" + RB"abc"', '    STRING     \'rb"abc"\'     (1, 0) (1, 7)\n    OP         \'+\'           (1, 8) (1, 9)\n    STRING     \'rB"abc"\'     (1, 10) (1, 17)\n    OP         \'+\'           (1, 18) (1, 19)\n    STRING     \'Rb"abc"\'     (1, 20) (1, 27)\n    OP         \'+\'           (1, 28) (1, 29)\n    STRING     \'RB"abc"\'     (1, 30) (1, 37)\n    ')
    TokenizeTest.check_tokenize('"a\\\nde\\\nfg"', '    STRING     \'"a\\\\\\nde\\\\\\nfg"\' (1, 0) (3, 3)\n    ')
    TokenizeTest.check_tokenize('u"a\\\nde"', '    STRING     \'u"a\\\\\\nde"\'  (1, 0) (2, 3)\n    ')
    TokenizeTest.check_tokenize('rb"a\\\nd"', '    STRING     \'rb"a\\\\\\nd"\'  (1, 0) (2, 2)\n    ')
    TokenizeTest.check_tokenize('"""a\\\nb"""', '    STRING     \'"""a\\\\\\nb"""\' (1, 0) (2, 4)\n    ')
    TokenizeTest.check_tokenize('u"""a\\\nb"""', '    STRING     \'u"""a\\\\\\nb"""\' (1, 0) (2, 4)\n    ')
    TokenizeTest.check_tokenize('rb"""a\\\nb\\\nc"""', '    STRING     \'rb"""a\\\\\\nb\\\\\\nc"""\' (1, 0) (3, 4)\n    ')
    TokenizeTest.check_tokenize('f"abc"', '    STRING     \'f"abc"\'      (1, 0) (1, 6)\n    ')
    TokenizeTest.check_tokenize('fR"a{b}c"', '    STRING     \'fR"a{b}c"\'   (1, 0) (1, 9)\n    ')
    TokenizeTest.check_tokenize('f"""abc"""', '    STRING     \'f"""abc"""\'  (1, 0) (1, 10)\n    ')
    TokenizeTest.check_tokenize('f"abc\\\ndef"', '    STRING     \'f"abc\\\\\\ndef"\' (1, 0) (2, 4)\n    ')
    TokenizeTest.check_tokenize('Rf"abc\\\ndef"', '    STRING     \'Rf"abc\\\\\\ndef"\' (1, 0) (2, 4)\n    ')

TokenizeTest = test_tokenize.TokenizeTest()
test_string()
