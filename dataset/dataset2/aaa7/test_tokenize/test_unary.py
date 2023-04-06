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

def test_unary():
    TokenizeTest.check_tokenize('~1 ^ 1 & 1 |1 ^ -1', "    OP         '~'           (1, 0) (1, 1)\n    NUMBER     '1'           (1, 1) (1, 2)\n    OP         '^'           (1, 3) (1, 4)\n    NUMBER     '1'           (1, 5) (1, 6)\n    OP         '&'           (1, 7) (1, 8)\n    NUMBER     '1'           (1, 9) (1, 10)\n    OP         '|'           (1, 11) (1, 12)\n    NUMBER     '1'           (1, 12) (1, 13)\n    OP         '^'           (1, 14) (1, 15)\n    OP         '-'           (1, 16) (1, 17)\n    NUMBER     '1'           (1, 17) (1, 18)\n    ")
    TokenizeTest.check_tokenize('-1*1/1+1*1//1 - ---1**1', "    OP         '-'           (1, 0) (1, 1)\n    NUMBER     '1'           (1, 1) (1, 2)\n    OP         '*'           (1, 2) (1, 3)\n    NUMBER     '1'           (1, 3) (1, 4)\n    OP         '/'           (1, 4) (1, 5)\n    NUMBER     '1'           (1, 5) (1, 6)\n    OP         '+'           (1, 6) (1, 7)\n    NUMBER     '1'           (1, 7) (1, 8)\n    OP         '*'           (1, 8) (1, 9)\n    NUMBER     '1'           (1, 9) (1, 10)\n    OP         '//'          (1, 10) (1, 12)\n    NUMBER     '1'           (1, 12) (1, 13)\n    OP         '-'           (1, 14) (1, 15)\n    OP         '-'           (1, 16) (1, 17)\n    OP         '-'           (1, 17) (1, 18)\n    OP         '-'           (1, 18) (1, 19)\n    NUMBER     '1'           (1, 19) (1, 20)\n    OP         '**'          (1, 20) (1, 22)\n    NUMBER     '1'           (1, 22) (1, 23)\n    ")

TokenizeTest = test_tokenize.TokenizeTest()
test_unary()
