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

def test_no_bom_no_encoding_cookie():
    lines = (b'# something\n', b'print(something)\n', b'do_something(else)\n')
    (encoding, consumed_lines) = detect_encoding(TestDetectEncoding.get_readline(lines))
    TestDetectEncoding.assertEqual(encoding, 'utf-8')
    TestDetectEncoding.assertEqual(consumed_lines, list(lines[:2]))

TestDetectEncoding = test_tokenize.TestDetectEncoding()
test_no_bom_no_encoding_cookie()
