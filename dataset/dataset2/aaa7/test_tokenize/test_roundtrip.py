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

def test_roundtrip():
    TestRoundtrip.check_roundtrip('if x == 1:\n    print(x)\n')
    TestRoundtrip.check_roundtrip('# This is a comment\n# This also\n')
    TestRoundtrip.check_roundtrip('if x == 1 : \n  print(x)\n')
    fn = support.findfile('tokenize_tests.txt')
    with open(fn, 'rb') as f:
        TestRoundtrip.check_roundtrip(f)
    TestRoundtrip.check_roundtrip('if x == 1:\n    # A comment by itTestRoundtrip.\n    print(x) # Comment here, too.\n    # Another comment.\nafter_if = True\n')
    TestRoundtrip.check_roundtrip("if (x # The comments need to go in the right place\n    == 1):\n    print('x==1')\n")
    TestRoundtrip.check_roundtrip('class Test: # A comment here\n  # A comment with weird indent\n  after_com = 5\n  def x(m): return m*5 # a one liner\n  def y(m): # A whitespace after the colon\n     return y*4 # 3-space indent\n')
    TestRoundtrip.check_roundtrip("try: import somemodule\nexcept ImportError: # comment\n    print('Can not import' # comment2\n)else:   print('Loaded')\n")

TestRoundtrip = test_tokenize.TestRoundtrip()
test_roundtrip()
