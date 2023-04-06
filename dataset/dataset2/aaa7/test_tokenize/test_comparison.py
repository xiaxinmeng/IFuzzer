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

def test_comparison():
    TokenizeTest.check_tokenize('if 1 < 1 > 1 == 1 >= 5 <= 0x15 <= 0x12 != 1 and 5 in 1 not in 1 is 1 or 5 is not 1: pass', "    NAME       'if'          (1, 0) (1, 2)\n    NUMBER     '1'           (1, 3) (1, 4)\n    OP         '<'           (1, 5) (1, 6)\n    NUMBER     '1'           (1, 7) (1, 8)\n    OP         '>'           (1, 9) (1, 10)\n    NUMBER     '1'           (1, 11) (1, 12)\n    OP         '=='          (1, 13) (1, 15)\n    NUMBER     '1'           (1, 16) (1, 17)\n    OP         '>='          (1, 18) (1, 20)\n    NUMBER     '5'           (1, 21) (1, 22)\n    OP         '<='          (1, 23) (1, 25)\n    NUMBER     '0x15'        (1, 26) (1, 30)\n    OP         '<='          (1, 31) (1, 33)\n    NUMBER     '0x12'        (1, 34) (1, 38)\n    OP         '!='          (1, 39) (1, 41)\n    NUMBER     '1'           (1, 42) (1, 43)\n    NAME       'and'         (1, 44) (1, 47)\n    NUMBER     '5'           (1, 48) (1, 49)\n    NAME       'in'          (1, 50) (1, 52)\n    NUMBER     '1'           (1, 53) (1, 54)\n    NAME       'not'         (1, 55) (1, 58)\n    NAME       'in'          (1, 59) (1, 61)\n    NUMBER     '1'           (1, 62) (1, 63)\n    NAME       'is'          (1, 64) (1, 66)\n    NUMBER     '1'           (1, 67) (1, 68)\n    NAME       'or'          (1, 69) (1, 71)\n    NUMBER     '5'           (1, 72) (1, 73)\n    NAME       'is'          (1, 74) (1, 76)\n    NAME       'not'         (1, 77) (1, 80)\n    NUMBER     '1'           (1, 81) (1, 82)\n    OP         ':'           (1, 82) (1, 83)\n    NAME       'pass'        (1, 84) (1, 88)\n    ")

TokenizeTest = test_tokenize.TokenizeTest()
test_comparison()
