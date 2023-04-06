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

def test_decistmt():
    from decimal import Decimal
    s = '+21.3e-5*-.1234/81.7'
    TestMisc.assertEqual(test_tokenize.decistmt(s), "+Decimal ('21.3e-5')*-Decimal ('.1234')/Decimal ('81.7')")
    TestMisc.assertRegex(repr(eval(s)), '-3.2171603427[0-9]*e-0+7')
    TestMisc.assertEqual(eval(test_tokenize.decistmt(s)), Decimal('-3.217160342717258261933904529E-7'))

TestMisc = test_tokenize.TestMisc()
test_decistmt()
