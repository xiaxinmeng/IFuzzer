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

def test_function():
    TokenizeTest.check_tokenize('def d22(a, b, c=2, d=2, *k): pass', "    NAME       'def'         (1, 0) (1, 3)\n    NAME       'd22'         (1, 4) (1, 7)\n    OP         '('           (1, 7) (1, 8)\n    NAME       'a'           (1, 8) (1, 9)\n    OP         ','           (1, 9) (1, 10)\n    NAME       'b'           (1, 11) (1, 12)\n    OP         ','           (1, 12) (1, 13)\n    NAME       'c'           (1, 14) (1, 15)\n    OP         '='           (1, 15) (1, 16)\n    NUMBER     '2'           (1, 16) (1, 17)\n    OP         ','           (1, 17) (1, 18)\n    NAME       'd'           (1, 19) (1, 20)\n    OP         '='           (1, 20) (1, 21)\n    NUMBER     '2'           (1, 21) (1, 22)\n    OP         ','           (1, 22) (1, 23)\n    OP         '*'           (1, 24) (1, 25)\n    NAME       'k'           (1, 25) (1, 26)\n    OP         ')'           (1, 26) (1, 27)\n    OP         ':'           (1, 27) (1, 28)\n    NAME       'pass'        (1, 29) (1, 33)\n    ")
    TokenizeTest.check_tokenize('def d01v_(a=1, *k, **w): pass', "    NAME       'def'         (1, 0) (1, 3)\n    NAME       'd01v_'       (1, 4) (1, 9)\n    OP         '('           (1, 9) (1, 10)\n    NAME       'a'           (1, 10) (1, 11)\n    OP         '='           (1, 11) (1, 12)\n    NUMBER     '1'           (1, 12) (1, 13)\n    OP         ','           (1, 13) (1, 14)\n    OP         '*'           (1, 15) (1, 16)\n    NAME       'k'           (1, 16) (1, 17)\n    OP         ','           (1, 17) (1, 18)\n    OP         '**'          (1, 19) (1, 21)\n    NAME       'w'           (1, 21) (1, 22)\n    OP         ')'           (1, 22) (1, 23)\n    OP         ':'           (1, 23) (1, 24)\n    NAME       'pass'        (1, 25) (1, 29)\n    ")
    TokenizeTest.check_tokenize('def d23(a: str, b: int=3) -> int: pass', "    NAME       'def'         (1, 0) (1, 3)\n    NAME       'd23'         (1, 4) (1, 7)\n    OP         '('           (1, 7) (1, 8)\n    NAME       'a'           (1, 8) (1, 9)\n    OP         ':'           (1, 9) (1, 10)\n    NAME       'str'         (1, 11) (1, 14)\n    OP         ','           (1, 14) (1, 15)\n    NAME       'b'           (1, 16) (1, 17)\n    OP         ':'           (1, 17) (1, 18)\n    NAME       'int'         (1, 19) (1, 22)\n    OP         '='           (1, 22) (1, 23)\n    NUMBER     '3'           (1, 23) (1, 24)\n    OP         ')'           (1, 24) (1, 25)\n    OP         '->'          (1, 26) (1, 28)\n    NAME       'int'         (1, 29) (1, 32)\n    OP         ':'           (1, 32) (1, 33)\n    NAME       'pass'        (1, 34) (1, 38)\n    ")

TokenizeTest = test_tokenize.TokenizeTest()
test_function()
