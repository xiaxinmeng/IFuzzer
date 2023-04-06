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

def test_indentation_semantics_retained():
    """
        Ensure that although whitespace might be mutated in a roundtrip,
        the semantic meaning of the indentation remains consistent.
        """
    code = 'if False:\n\tx=3\n\tx=3\n'
    codelines = TestRoundtrip.roundtrip(code).split('\n')
    TestRoundtrip.assertEqual(codelines[1], codelines[2])
    TestRoundtrip.check_roundtrip(code)

TestRoundtrip = test_tokenize.TestRoundtrip()
test_indentation_semantics_retained()
