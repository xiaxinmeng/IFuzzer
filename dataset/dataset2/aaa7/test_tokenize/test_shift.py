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

def test_shift():
    TokenizeTest.check_tokenize('x = 1 << 1 >> 5', "    NAME       'x'           (1, 0) (1, 1)\n    OP         '='           (1, 2) (1, 3)\n    NUMBER     '1'           (1, 4) (1, 5)\n    OP         '<<'          (1, 6) (1, 8)\n    NUMBER     '1'           (1, 9) (1, 10)\n    OP         '>>'          (1, 11) (1, 13)\n    NUMBER     '5'           (1, 14) (1, 15)\n    ")

TokenizeTest = test_tokenize.TokenizeTest()
test_shift()
