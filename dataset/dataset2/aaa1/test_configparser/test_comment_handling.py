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

def test_comment_handling():
    config_string = textwrap.dedent('        [Commented Bar]\n        baz=qwe ; a comment\n        foo: bar # not a comment!\n        # but this is a comment\n        ; another comment\n        quirk: this;is not a comment\n        ; a space must precede an inline comment\n        ')
    cf = CompatibleTestCase.fromstring(config_string)
    CompatibleTestCase.assertEqual(cf.get('Commented Bar', 'foo'), 'bar # not a comment!')
    CompatibleTestCase.assertEqual(cf.get('Commented Bar', 'baz'), 'qwe')
    CompatibleTestCase.assertEqual(cf.get('Commented Bar', 'quirk'), 'this;is not a comment')

CompatibleTestCase = test_configparser.CompatibleTestCase()
test_comment_handling()
