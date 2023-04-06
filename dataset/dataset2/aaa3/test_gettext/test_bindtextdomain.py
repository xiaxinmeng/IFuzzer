import os
import base64
import contextlib
import gettext
import unittest
from test import support
from test.support import os_helper
import builtins
import test_gettext

def test_bindtextdomain():
    GettextTestCase2.assertEqual(gettext.bindtextdomain('gettext'), GettextTestCase2.localedir)

GettextTestCase2 = test_gettext.GettextTestCase2()
GettextTestCase2.setUp()
test_bindtextdomain()
