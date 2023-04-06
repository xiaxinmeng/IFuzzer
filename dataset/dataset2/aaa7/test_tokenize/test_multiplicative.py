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

def test_multiplicative():
    TokenizeTest.check_tokenize('x = 1//1*1/5*12%0x12@42', "    NAME       'x'           (1, 0) (1, 1)\n    OP         '='           (1, 2) (1, 3)\n    NUMBER     '1'           (1, 4) (1, 5)\n    OP         '//'          (1, 5) (1, 7)\n    NUMBER     '1'           (1, 7) (1, 8)\n    OP         '*'           (1, 8) (1, 9)\n    NUMBER     '1'           (1, 9) (1, 10)\n    OP         '/'           (1, 10) (1, 11)\n    NUMBER     '5'           (1, 11) (1, 12)\n    OP         '*'           (1, 12) (1, 13)\n    NUMBER     '12'          (1, 13) (1, 15)\n    OP         '%'           (1, 15) (1, 16)\n    NUMBER     '0x12'        (1, 16) (1, 20)\n    OP         '@'           (1, 20) (1, 21)\n    NUMBER     '42'          (1, 21) (1, 23)\n    ")

TokenizeTest = test_tokenize.TokenizeTest()
test_multiplicative()
