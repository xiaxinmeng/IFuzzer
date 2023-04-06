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

def test_basic():
    TokenizeTest.check_tokenize('1 + 1', "    NUMBER     '1'           (1, 0) (1, 1)\n    OP         '+'           (1, 2) (1, 3)\n    NUMBER     '1'           (1, 4) (1, 5)\n    ")
    TokenizeTest.check_tokenize('if False:\n    # NL\n    \n    True = False # NEWLINE\n', "    NAME       'if'          (1, 0) (1, 2)\n    NAME       'False'       (1, 3) (1, 8)\n    OP         ':'           (1, 8) (1, 9)\n    NEWLINE    '\\n'          (1, 9) (1, 10)\n    COMMENT    '# NL'        (2, 4) (2, 8)\n    NL         '\\n'          (2, 8) (2, 9)\n    NL         '\\n'          (3, 4) (3, 5)\n    INDENT     '    '        (4, 0) (4, 4)\n    NAME       'True'        (4, 4) (4, 8)\n    OP         '='           (4, 9) (4, 10)\n    NAME       'False'       (4, 11) (4, 16)\n    COMMENT    '# NEWLINE'   (4, 17) (4, 26)\n    NEWLINE    '\\n'          (4, 26) (4, 27)\n    DEDENT     ''            (5, 0) (5, 0)\n    ")
    indent_error_file = b'def k(x):\n    x += 2\n  x += 5\n'
    readline = BytesIO(indent_error_file).readline
    with TokenizeTest.assertRaisesRegex(IndentationError, 'unindent does not match any outer indentation level'):
        for tok in tokenize(readline):
            pass

TokenizeTest = test_tokenize.TokenizeTest()
test_basic()
