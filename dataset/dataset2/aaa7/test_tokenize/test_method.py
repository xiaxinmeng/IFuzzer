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

def test_method():
    TokenizeTest.check_tokenize('@staticmethod\ndef foo(x,y): pass', "    OP         '@'           (1, 0) (1, 1)\n    NAME       'staticmethod' (1, 1) (1, 13)\n    NEWLINE    '\\n'          (1, 13) (1, 14)\n    NAME       'def'         (2, 0) (2, 3)\n    NAME       'foo'         (2, 4) (2, 7)\n    OP         '('           (2, 7) (2, 8)\n    NAME       'x'           (2, 8) (2, 9)\n    OP         ','           (2, 9) (2, 10)\n    NAME       'y'           (2, 10) (2, 11)\n    OP         ')'           (2, 11) (2, 12)\n    OP         ':'           (2, 12) (2, 13)\n    NAME       'pass'        (2, 14) (2, 18)\n    ")

TokenizeTest = test_tokenize.TokenizeTest()
test_method()
