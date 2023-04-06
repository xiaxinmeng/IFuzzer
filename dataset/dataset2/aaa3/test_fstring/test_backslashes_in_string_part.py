import ast
import os
import re
import types
import decimal
import unittest
from test.support.os_helper import temp_cwd
from test.support.script_helper import assert_python_failure
import test_fstring

def test_backslashes_in_string_part():
    TestCase.assertEqual(f'\t', '\t')
    TestCase.assertEqual('\\t', '\\t')
    TestCase.assertEqual(f'\\t', '\\t')
    TestCase.assertEqual(f'{2}\t', '2\t')
    TestCase.assertEqual(f'{2}\t{3}', '2\t3')
    TestCase.assertEqual(f'\t{3}', '\t3')
    TestCase.assertEqual(f'Δ', 'Δ')
    TestCase.assertEqual('\\u0394', '\\u0394')
    TestCase.assertEqual(f'\\u0394', '\\u0394')
    TestCase.assertEqual(f'{2}Δ', '2Δ')
    TestCase.assertEqual(f'{2}Δ{3}', '2Δ3')
    TestCase.assertEqual(f'Δ{3}', 'Δ3')
    TestCase.assertEqual(f'Δ', 'Δ')
    TestCase.assertEqual('\\U00000394', '\\U00000394')
    TestCase.assertEqual(f'\\U00000394', '\\U00000394')
    TestCase.assertEqual(f'{2}Δ', '2Δ')
    TestCase.assertEqual(f'{2}Δ{3}', '2Δ3')
    TestCase.assertEqual(f'Δ{3}', 'Δ3')
    TestCase.assertEqual(f'Δ', 'Δ')
    TestCase.assertEqual(f'{2}Δ', '2Δ')
    TestCase.assertEqual(f'{2}Δ{3}', '2Δ3')
    TestCase.assertEqual(f'Δ{3}', 'Δ3')
    TestCase.assertEqual(f'2Δ', '2Δ')
    TestCase.assertEqual(f'2Δ3', '2Δ3')
    TestCase.assertEqual(f'Δ3', 'Δ3')
    TestCase.assertEqual(f' ', ' ')
    TestCase.assertEqual('\\x20', '\\x20')
    TestCase.assertEqual(f'\\x20', '\\x20')
    TestCase.assertEqual(f'{2} ', '2 ')
    TestCase.assertEqual(f'{2} {3}', '2 3')
    TestCase.assertEqual(f' {3}', ' 3')
    TestCase.assertEqual(f'2 ', '2 ')
    TestCase.assertEqual(f'2 3', '2 3')
    TestCase.assertEqual(f' 3', ' 3')
    with TestCase.assertWarns(DeprecationWarning):
        value = eval("f'\\{6*7}'")
    TestCase.assertEqual(value, '\\42')
    TestCase.assertEqual(f'\\{6 * 7}', '\\42')
    TestCase.assertEqual(f'\\{6 * 7}', '\\42')
    AMPERSAND = 'spam'
    TestCase.assertEqual(f'&', '&')
    TestCase.assertEqual(f'\\N{AMPERSAND}', '\\Nspam')
    TestCase.assertEqual(f'\\N{AMPERSAND}', '\\Nspam')
    TestCase.assertEqual(f'\\&', '\\&')

TestCase = test_fstring.TestCase()
test_backslashes_in_string_part()
