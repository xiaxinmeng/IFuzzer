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

def test_selector():
    TokenizeTest.check_tokenize("import sys, time\nx = sys.modules['time'].time()", '    NAME       \'import\'      (1, 0) (1, 6)\n    NAME       \'sys\'         (1, 7) (1, 10)\n    OP         \',\'           (1, 10) (1, 11)\n    NAME       \'time\'        (1, 12) (1, 16)\n    NEWLINE    \'\\n\'          (1, 16) (1, 17)\n    NAME       \'x\'           (2, 0) (2, 1)\n    OP         \'=\'           (2, 2) (2, 3)\n    NAME       \'sys\'         (2, 4) (2, 7)\n    OP         \'.\'           (2, 7) (2, 8)\n    NAME       \'modules\'     (2, 8) (2, 15)\n    OP         \'[\'           (2, 15) (2, 16)\n    STRING     "\'time\'"      (2, 16) (2, 22)\n    OP         \']\'           (2, 22) (2, 23)\n    OP         \'.\'           (2, 23) (2, 24)\n    NAME       \'time\'        (2, 24) (2, 28)\n    OP         \'(\'           (2, 28) (2, 29)\n    OP         \')\'           (2, 29) (2, 30)\n    ')

TokenizeTest = test_tokenize.TokenizeTest()
test_selector()
