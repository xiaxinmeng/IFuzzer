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

def test_float():
    TokenizeTest.check_tokenize('x = 3.14159', "    NAME       'x'           (1, 0) (1, 1)\n    OP         '='           (1, 2) (1, 3)\n    NUMBER     '3.14159'     (1, 4) (1, 11)\n    ")
    TokenizeTest.check_tokenize('x = 314159.', "    NAME       'x'           (1, 0) (1, 1)\n    OP         '='           (1, 2) (1, 3)\n    NUMBER     '314159.'     (1, 4) (1, 11)\n    ")
    TokenizeTest.check_tokenize('x = .314159', "    NAME       'x'           (1, 0) (1, 1)\n    OP         '='           (1, 2) (1, 3)\n    NUMBER     '.314159'     (1, 4) (1, 11)\n    ")
    TokenizeTest.check_tokenize('x = 3e14159', "    NAME       'x'           (1, 0) (1, 1)\n    OP         '='           (1, 2) (1, 3)\n    NUMBER     '3e14159'     (1, 4) (1, 11)\n    ")
    TokenizeTest.check_tokenize('x = 3E123', "    NAME       'x'           (1, 0) (1, 1)\n    OP         '='           (1, 2) (1, 3)\n    NUMBER     '3E123'       (1, 4) (1, 9)\n    ")
    TokenizeTest.check_tokenize('x+y = 3e-1230', "    NAME       'x'           (1, 0) (1, 1)\n    OP         '+'           (1, 1) (1, 2)\n    NAME       'y'           (1, 2) (1, 3)\n    OP         '='           (1, 4) (1, 5)\n    NUMBER     '3e-1230'     (1, 6) (1, 13)\n    ")
    TokenizeTest.check_tokenize('x = 3.14e159', "    NAME       'x'           (1, 0) (1, 1)\n    OP         '='           (1, 2) (1, 3)\n    NUMBER     '3.14e159'    (1, 4) (1, 12)\n    ")

TokenizeTest = test_tokenize.TokenizeTest()
test_float()
