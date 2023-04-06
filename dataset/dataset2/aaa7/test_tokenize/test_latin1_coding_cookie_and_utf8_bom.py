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

def test_latin1_coding_cookie_and_utf8_bom():
    """
        As per PEP 0263, if a file starts with a utf-8 BOM signature, the only
        allowed encoding for the comment is 'utf-8'.  The text file used in
        this test starts with a BOM signature, but specifies latin1 as the
        coding, so verify that a SyntaxError is raised, which matches the
        behaviour of the interpreter when it encounters a similar condition.
        """
    f = 'tokenize_tests-latin1-coding-cookie-and-utf8-bom-sig.txt'
    TestTokenizerAdheresToPep0263.assertRaises(SyntaxError, TestTokenizerAdheresToPep0263._testFile, f)

TestTokenizerAdheresToPep0263 = test_tokenize.TestTokenizerAdheresToPep0263()
test_latin1_coding_cookie_and_utf8_bom()
