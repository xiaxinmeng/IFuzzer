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

def test_bad_input_order():
    u = Untokenizer()
    u.prev_row = 2
    u.prev_col = 2
    with UntokenizeTest.assertRaises(ValueError) as cm:
        u.add_whitespace((1, 3))
    UntokenizeTest.assertEqual(cm.exception.args[0], 'start (1,3) precedes previous end (2,2)')
    UntokenizeTest.assertRaises(ValueError, u.add_whitespace, (2, 1))

UntokenizeTest = test_tokenize.UntokenizeTest()
test_bad_input_order()
