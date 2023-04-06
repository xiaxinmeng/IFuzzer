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

def test_non_ascii_identifiers():
    TokenizeTest.check_tokenize("Örter = 'places'\ngrün = 'green'", '    NAME       \'Örter\'       (1, 0) (1, 5)\n    OP         \'=\'           (1, 6) (1, 7)\n    STRING     "\'places\'"    (1, 8) (1, 16)\n    NEWLINE    \'\\n\'          (1, 16) (1, 17)\n    NAME       \'grün\'        (2, 0) (2, 4)\n    OP         \'=\'           (2, 5) (2, 6)\n    STRING     "\'green\'"     (2, 7) (2, 14)\n    ')

TokenizeTest = test_tokenize.TokenizeTest()
test_non_ascii_identifiers()
