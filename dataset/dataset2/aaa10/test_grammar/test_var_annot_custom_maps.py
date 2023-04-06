from test.support import check_syntax_error
from test.support.warnings_helper import check_syntax_warning
import inspect
import unittest
import sys
import warnings
from sys import *
import test.ann_module as ann_module
import typing
from collections import ChainMap
from test import ann_module2
import test
from test.support import check_syntax_error
from sys import maxsize
from test.support import check_syntax_error
from test.support.warnings_helper import check_syntax_warning
from test.ann_module3 import f_bad_ann, g_bad_ann, D_bad_ann
import sys
import time, sys
from time import time
from time import time
from sys import path, argv
from sys import path, argv
from sys import path, argv
import sys, time
import test_grammar

def test_var_annot_custom_maps():
    ns = {'__annotations__': test_grammar.CNS()}
    exec('X: int; Z: str = "Z"; (w): complex = 1j', ns)
    GrammarTests.assertEqual(ns['__annotations__']['x'], 'int')
    GrammarTests.assertEqual(ns['__annotations__']['z'], 'str')
    with GrammarTests.assertRaises(KeyError):
        ns['__annotations__']['w']
    nonloc_ns = {}

    class CNS2:

        def __init__(GrammarTests):
            GrammarTests._dct = {}

        def __setitem__(GrammarTests, item, value):
            nonlocal nonloc_ns
            GrammarTests._dct[item] = value
            nonloc_ns[item] = value

        def __getitem__(GrammarTests, item):
            return GrammarTests._dct[item]
    exec('x: int = 1', {}, CNS2())
    GrammarTests.assertEqual(nonloc_ns['__annotations__']['x'], 'int')

GrammarTests = test_grammar.GrammarTests()
test_var_annot_custom_maps()
