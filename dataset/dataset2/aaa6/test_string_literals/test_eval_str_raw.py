import os
import sys
import shutil
import tempfile
import unittest
import warnings
import test_string_literals

def test_eval_str_raw():
    TestLiterals.assertEqual(eval(" r'x' "), 'x')
    TestLiterals.assertEqual(eval(" r'\\x01' "), '\\' + 'x01')
    TestLiterals.assertEqual(eval(" r'\x01' "), chr(1))
    TestLiterals.assertEqual(eval(" r'\\x81' "), '\\' + 'x81')
    TestLiterals.assertEqual(eval(" r'\x81' "), chr(129))
    TestLiterals.assertEqual(eval(" r'\\u1881' "), '\\' + 'u1881')
    TestLiterals.assertEqual(eval(" r'ᢁ' "), chr(6273))
    TestLiterals.assertEqual(eval(" r'\\U0001d120' "), '\\' + 'U0001d120')
    TestLiterals.assertEqual(eval(" r'𝄠' "), chr(119072))

TestLiterals = test_string_literals.TestLiterals()
test_eval_str_raw()
