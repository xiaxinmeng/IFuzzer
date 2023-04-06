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

def test_long():
    TokenizeTest.check_tokenize('x = 0', "    NAME       'x'           (1, 0) (1, 1)\n    OP         '='           (1, 2) (1, 3)\n    NUMBER     '0'           (1, 4) (1, 5)\n    ")
    TokenizeTest.check_tokenize('x = 0xfffffffffff', "    NAME       'x'           (1, 0) (1, 1)\n    OP         '='           (1, 2) (1, 3)\n    NUMBER     '0xfffffffffff' (1, 4) (1, 17)\n    ")
    TokenizeTest.check_tokenize('x = 123141242151251616110', "    NAME       'x'           (1, 0) (1, 1)\n    OP         '='           (1, 2) (1, 3)\n    NUMBER     '123141242151251616110' (1, 4) (1, 25)\n    ")
    TokenizeTest.check_tokenize('x = -15921590215012591', "    NAME       'x'           (1, 0) (1, 1)\n    OP         '='           (1, 2) (1, 3)\n    OP         '-'           (1, 4) (1, 5)\n    NUMBER     '15921590215012591' (1, 5) (1, 22)\n    ")

TokenizeTest = test_tokenize.TokenizeTest()
test_long()
