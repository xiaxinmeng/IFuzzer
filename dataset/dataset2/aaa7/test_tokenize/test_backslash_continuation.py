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

def test_backslash_continuation():
    UntokenizeTest.check_roundtrip('x=1+\\\n1\n# This is a comment\\\n# This also\n')
    UntokenizeTest.check_roundtrip('# Comment \\\nx = 0')

UntokenizeTest = test_tokenize.UntokenizeTest()
UntokenizeTest.setUp()
test_backslash_continuation()
