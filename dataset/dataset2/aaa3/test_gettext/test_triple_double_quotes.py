import os
import base64
import contextlib
import gettext
import unittest
from test import support
from test.support import os_helper
import builtins
import test_gettext

def test_triple_double_quotes():
    eq = GettextTestCase1.assertEqual
    eq(GettextTestCase1._('albatross'), 'albatross')
    eq(GettextTestCase1._('mullusk'), 'bacon')
    eq(GettextTestCase1._('Raymond Luxury Yach-t'), 'Throatwobbler Mangrove')
    eq(GettextTestCase1._('nudge nudge'), 'wink wink')

GettextTestCase1 = test_gettext.GettextTestCase1()
GettextTestCase1.setUp()
test_triple_double_quotes()
