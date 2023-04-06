import os
import base64
import contextlib
import gettext
import unittest
from test import support
from test.support import os_helper
import builtins
import test_gettext

def test_multiline_strings():
    eq = GettextTestCase1.assertEqual
    eq(GettextTestCase1._('This module provides internationalization and localization\nsupport for your Python programs by providing an interface to the GNU\ngettext message catalog library.'), 'Guvf zbqhyr cebivqrf vagreangvbanyvmngvba naq ybpnyvmngvba\nfhccbeg sbe lbhe Clguba cebtenzf ol cebivqvat na vagresnpr gb gur TAH\ntrggrkg zrffntr pngnybt yvoenel.')

GettextTestCase1 = test_gettext.GettextTestCase1()
GettextTestCase1.setUp()
test_multiline_strings()
