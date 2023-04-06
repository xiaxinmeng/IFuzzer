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

def test_continuation():
    TestRoundtrip.check_roundtrip("a = (3,4, \n5,6)\ny = [3, 4,\n5]\nz = {'a': 5,\n'b':15, 'c':True}\nx = len(y) + 5 - a[\n3] - a[2]\n+ len(z) - z[\n'b']\n")

TestRoundtrip = test_tokenize.TestRoundtrip()
test_continuation()
