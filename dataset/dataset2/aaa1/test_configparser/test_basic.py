import collections
import configparser
import io
import os
import pathlib
import textwrap
import unittest
import warnings
from test import support
from test.support import os_helper
import decimal
import pickle
import pickle
import pickle
import pickle
import pickle
import pickle
import pickle
import pickle
import pickle
import pickle
import pickle
import decimal
import test_configparser

def test_basic():
    config_string = '[Foo Bar]\nfoo{0[0]}bar1\n[Spacey Bar]\nfoo {0[0]} bar2\n[Spacey Bar From The Beginning]\n  foo {0[0]} bar3\n  baz {0[0]} qwe\n[Commented Bar]\nfoo{0[1]} bar4 {1[1]} comment\nbaz{0[0]}qwe {1[0]}another one\n[Long Line]\nfoo{0[1]} this line is much, much longer than my editor\n   likes it.\n[Section\\with$weird%characters[\t]\n[Internationalized Stuff]\nfoo[bg]{0[1]} Bulgarian\nfoo{0[0]}Default\nfoo[en]{0[0]}English\nfoo[de]{0[0]}Deutsch\n[Spaces]\nkey with spaces {0[1]} value\nanother with spaces {0[0]} splat!\n[Types]\nint {0[1]} 42\nfloat {0[0]} 0.44\nboolean {0[0]} NO\n123 {0[1]} strange but acceptable\n'.format(BasicTestCase.delimiters, BasicTestCase.comment_prefixes)
    if BasicTestCase.allow_no_value:
        config_string += '[NoValue]\noption-without-value\n'
    cf = BasicTestCase.fromstring(config_string)
    BasicTestCase.basic_test(cf)
    if BasicTestCase.strict:
        with BasicTestCase.assertRaises(configparser.DuplicateOptionError):
            cf.read_string(textwrap.dedent('                    [Duplicate Options Here]\n                    option {0[0]} with a value\n                    option {0[1]} with another value\n                '.format(BasicTestCase.delimiters)))
        with BasicTestCase.assertRaises(configparser.DuplicateSectionError):
            cf.read_string(textwrap.dedent('                    [And Now For Something]\n                    completely different {0[0]} True\n                    [And Now For Something]\n                    the larch {0[1]} 1\n                '.format(BasicTestCase.delimiters)))
    else:
        cf.read_string(textwrap.dedent('                [Duplicate Options Here]\n                option {0[0]} with a value\n                option {0[1]} with another value\n            '.format(BasicTestCase.delimiters)))
        cf.read_string(textwrap.dedent('                [And Now For Something]\n                completely different {0[0]} True\n                [And Now For Something]\n                the larch {0[1]} 1\n            '.format(BasicTestCase.delimiters)))

BasicTestCase = test_configparser.BasicTestCase()

test_basic()
