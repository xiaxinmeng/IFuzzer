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

def test_cookie_first_line_no_bom():
    lines = (b'# -*- coding: latin-1 -*-\n', b'print(something)\n', b'do_something(else)\n')
    (encoding, consumed_lines) = detect_encoding(TestDetectEncoding.get_readline(lines))
    TestDetectEncoding.assertEqual(encoding, 'iso-8859-1')
    TestDetectEncoding.assertEqual(consumed_lines, [b'# -*- coding: latin-1 -*-\n'])

TestDetectEncoding = test_tokenize.TestDetectEncoding()
test_cookie_first_line_no_bom()
