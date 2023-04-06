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

def test_mismatched_bom_and_cookie_first_line_raises_syntaxerror():
    lines = (b'\xef\xbb\xbf# vim: set fileencoding=ascii :\n', b'print(something)\n', b'do_something(else)\n')
    readline = TestDetectEncoding.get_readline(lines)
    TestDetectEncoding.assertRaises(SyntaxError, detect_encoding, readline)

TestDetectEncoding = test_tokenize.TestDetectEncoding()
test_mismatched_bom_and_cookie_first_line_raises_syntaxerror()
