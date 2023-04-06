import os
import sys
import shutil
import tempfile
import unittest
import warnings
import test_string_literals

def test_eval_str_normal():
    TestLiterals.assertEqual(eval(" 'x' "), 'x')
    TestLiterals.assertEqual(eval(" '\\x01' "), chr(1))
    TestLiterals.assertEqual(eval(" '\x01' "), chr(1))
    TestLiterals.assertEqual(eval(" '\\x81' "), chr(129))
    TestLiterals.assertEqual(eval(" '\x81' "), chr(129))
    TestLiterals.assertEqual(eval(" '\\u1881' "), chr(6273))
    TestLiterals.assertEqual(eval(" 'ᢁ' "), chr(6273))
    TestLiterals.assertEqual(eval(" '\\U0001d120' "), chr(119072))
    TestLiterals.assertEqual(eval(" '𝄠' "), chr(119072))

TestLiterals = test_string_literals.TestLiterals()
test_eval_str_normal()
