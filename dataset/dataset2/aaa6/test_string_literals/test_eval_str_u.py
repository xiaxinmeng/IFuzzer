import os
import sys
import shutil
import tempfile
import unittest
import warnings
import test_string_literals

def test_eval_str_u():
    TestLiterals.assertEqual(eval(" u'x' "), 'x')
    TestLiterals.assertEqual(eval(" U'ä' "), 'ä')
    TestLiterals.assertEqual(eval(" u'ä' "), 'ä')
    TestLiterals.assertRaises(SyntaxError, eval, " ur'' ")
    TestLiterals.assertRaises(SyntaxError, eval, " ru'' ")
    TestLiterals.assertRaises(SyntaxError, eval, " bu'' ")
    TestLiterals.assertRaises(SyntaxError, eval, " ub'' ")

TestLiterals = test_string_literals.TestLiterals()
test_eval_str_u()
