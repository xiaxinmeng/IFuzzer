import os
import base64
import contextlib
import gettext
import unittest
from test import support
from test.support import os_helper
import builtins
import test_gettext

def test_textdomain():
    GettextTestCase2.assertEqual(gettext.textdomain(), 'gettext')

GettextTestCase2 = test_gettext.GettextTestCase2()
test_textdomain()
