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

def test_additive():
    TokenizeTest.check_tokenize('x = 1 - y + 15 - 1 + 0x124 + z + a[5]', "    NAME       'x'           (1, 0) (1, 1)\n    OP         '='           (1, 2) (1, 3)\n    NUMBER     '1'           (1, 4) (1, 5)\n    OP         '-'           (1, 6) (1, 7)\n    NAME       'y'           (1, 8) (1, 9)\n    OP         '+'           (1, 10) (1, 11)\n    NUMBER     '15'          (1, 12) (1, 14)\n    OP         '-'           (1, 15) (1, 16)\n    NUMBER     '1'           (1, 17) (1, 18)\n    OP         '+'           (1, 19) (1, 20)\n    NUMBER     '0x124'       (1, 21) (1, 26)\n    OP         '+'           (1, 27) (1, 28)\n    NAME       'z'           (1, 29) (1, 30)\n    OP         '+'           (1, 31) (1, 32)\n    NAME       'a'           (1, 33) (1, 34)\n    OP         '['           (1, 34) (1, 35)\n    NUMBER     '5'           (1, 35) (1, 36)\n    OP         ']'           (1, 36) (1, 37)\n    ")

TokenizeTest = test_tokenize.TokenizeTest()
test_additive()
