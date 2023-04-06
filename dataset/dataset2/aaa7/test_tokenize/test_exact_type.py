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

def test_exact_type():
    TestTokenize.assertExactTypeEqual('()', token.LPAR, token.RPAR)
    TestTokenize.assertExactTypeEqual('[]', token.LSQB, token.RSQB)
    TestTokenize.assertExactTypeEqual(':', token.COLON)
    TestTokenize.assertExactTypeEqual(',', token.COMMA)
    TestTokenize.assertExactTypeEqual(';', token.SEMI)
    TestTokenize.assertExactTypeEqual('+', token.PLUS)
    TestTokenize.assertExactTypeEqual('-', token.MINUS)
    TestTokenize.assertExactTypeEqual('*', token.STAR)
    TestTokenize.assertExactTypeEqual('/', token.SLASH)
    TestTokenize.assertExactTypeEqual('|', token.VBAR)
    TestTokenize.assertExactTypeEqual('&', token.AMPER)
    TestTokenize.assertExactTypeEqual('<', token.LESS)
    TestTokenize.assertExactTypeEqual('>', token.GREATER)
    TestTokenize.assertExactTypeEqual('=', token.EQUAL)
    TestTokenize.assertExactTypeEqual('.', token.DOT)
    TestTokenize.assertExactTypeEqual('%', token.PERCENT)
    TestTokenize.assertExactTypeEqual('{}', token.LBRACE, token.RBRACE)
    TestTokenize.assertExactTypeEqual('==', token.EQEQUAL)
    TestTokenize.assertExactTypeEqual('!=', token.NOTEQUAL)
    TestTokenize.assertExactTypeEqual('<=', token.LESSEQUAL)
    TestTokenize.assertExactTypeEqual('>=', token.GREATEREQUAL)
    TestTokenize.assertExactTypeEqual('~', token.TILDE)
    TestTokenize.assertExactTypeEqual('^', token.CIRCUMFLEX)
    TestTokenize.assertExactTypeEqual('<<', token.LEFTSHIFT)
    TestTokenize.assertExactTypeEqual('>>', token.RIGHTSHIFT)
    TestTokenize.assertExactTypeEqual('**', token.DOUBLESTAR)
    TestTokenize.assertExactTypeEqual('+=', token.PLUSEQUAL)
    TestTokenize.assertExactTypeEqual('-=', token.MINEQUAL)
    TestTokenize.assertExactTypeEqual('*=', token.STAREQUAL)
    TestTokenize.assertExactTypeEqual('/=', token.SLASHEQUAL)
    TestTokenize.assertExactTypeEqual('%=', token.PERCENTEQUAL)
    TestTokenize.assertExactTypeEqual('&=', token.AMPEREQUAL)
    TestTokenize.assertExactTypeEqual('|=', token.VBAREQUAL)
    TestTokenize.assertExactTypeEqual('^=', token.CIRCUMFLEXEQUAL)
    TestTokenize.assertExactTypeEqual('^=', token.CIRCUMFLEXEQUAL)
    TestTokenize.assertExactTypeEqual('<<=', token.LEFTSHIFTEQUAL)
    TestTokenize.assertExactTypeEqual('>>=', token.RIGHTSHIFTEQUAL)
    TestTokenize.assertExactTypeEqual('**=', token.DOUBLESTAREQUAL)
    TestTokenize.assertExactTypeEqual('//', token.DOUBLESLASH)
    TestTokenize.assertExactTypeEqual('//=', token.DOUBLESLASHEQUAL)
    TestTokenize.assertExactTypeEqual(':=', token.COLONEQUAL)
    TestTokenize.assertExactTypeEqual('...', token.ELLIPSIS)
    TestTokenize.assertExactTypeEqual('->', token.RARROW)
    TestTokenize.assertExactTypeEqual('@', token.AT)
    TestTokenize.assertExactTypeEqual('@=', token.ATEQUAL)
    TestTokenize.assertExactTypeEqual('a**2+b**2==c**2', NAME, token.DOUBLESTAR, NUMBER, token.PLUS, NAME, token.DOUBLESTAR, NUMBER, token.EQEQUAL, NAME, token.DOUBLESTAR, NUMBER)
    TestTokenize.assertExactTypeEqual('{1, 2, 3}', token.LBRACE, token.NUMBER, token.COMMA, token.NUMBER, token.COMMA, token.NUMBER, token.RBRACE)
    TestTokenize.assertExactTypeEqual('^(x & 0x1)', token.CIRCUMFLEX, token.LPAR, token.NAME, token.AMPER, token.NUMBER, token.RPAR)

TestTokenize = test_tokenize.TestTokenize()
test_exact_type()
