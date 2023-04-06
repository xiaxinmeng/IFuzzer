import os
import sys
import shutil
import tempfile
import unittest
import warnings
import test_string_literals

def test_eval_bytes_normal():
    TestLiterals.assertEqual(eval(" b'x' "), b'x')
    TestLiterals.assertEqual(eval(" b'\\x01' "), test_string_literals.byte(1))
    TestLiterals.assertEqual(eval(" b'\x01' "), test_string_literals.byte(1))
    TestLiterals.assertEqual(eval(" b'\\x81' "), test_string_literals.byte(129))
    TestLiterals.assertRaises(SyntaxError, eval, " b'\x81' ")
    TestLiterals.assertEqual(eval(" br'\\u1881' "), b'\\' + b'u1881')
    TestLiterals.assertRaises(SyntaxError, eval, " b'ᢁ' ")
    TestLiterals.assertEqual(eval(" br'\\U0001d120' "), b'\\' + b'U0001d120')
    TestLiterals.assertRaises(SyntaxError, eval, " b'𝄠' ")

TestLiterals = test_string_literals.TestLiterals()
test_eval_bytes_normal()
