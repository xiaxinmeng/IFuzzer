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

def test_implicit_newline():
    f = BytesIO('x'.encode('utf-8'))
    tokens = list(tokenize(f.readline))
    TokenizeTest.assertEqual(tokens[-2].type, NEWLINE)
    TokenizeTest.assertEqual(tokens[-1].type, ENDMARKER)

TokenizeTest = test_tokenize.TokenizeTest()
test_implicit_newline()
