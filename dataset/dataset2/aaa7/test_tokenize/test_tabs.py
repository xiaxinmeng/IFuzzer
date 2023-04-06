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

def test_tabs():
    TokenizeTest.check_tokenize('def f():\n\tif x\n        \tpass', "    NAME       'def'         (1, 0) (1, 3)\n    NAME       'f'           (1, 4) (1, 5)\n    OP         '('           (1, 5) (1, 6)\n    OP         ')'           (1, 6) (1, 7)\n    OP         ':'           (1, 7) (1, 8)\n    NEWLINE    '\\n'          (1, 8) (1, 9)\n    INDENT     '\\t'          (2, 0) (2, 1)\n    NAME       'if'          (2, 1) (2, 3)\n    NAME       'x'           (2, 4) (2, 5)\n    NEWLINE    '\\n'          (2, 5) (2, 6)\n    INDENT     '        \\t'  (3, 0) (3, 9)\n    NAME       'pass'        (3, 9) (3, 13)\n    DEDENT     ''            (4, 0) (4, 0)\n    DEDENT     ''            (4, 0) (4, 0)\n    ")

TokenizeTest = test_tokenize.TokenizeTest()
test_tabs()
