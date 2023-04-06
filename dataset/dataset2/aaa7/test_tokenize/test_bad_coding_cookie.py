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

def test_bad_coding_cookie():
    TestTokenizerAdheresToPep0263.assertRaises(SyntaxError, TestTokenizerAdheresToPep0263._testFile, 'bad_coding.py')
    TestTokenizerAdheresToPep0263.assertRaises(SyntaxError, TestTokenizerAdheresToPep0263._testFile, 'bad_coding2.py')

TestTokenizerAdheresToPep0263 = test_tokenize.TestTokenizerAdheresToPep0263()
test_bad_coding_cookie()
